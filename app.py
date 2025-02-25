from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

DATABASE = 'database.db'

def format_datetime(value):
    if value:
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S").strftime("%d %b %Y, %H:%M:%S")
    return "N/A"

app.jinja_env.filters['format_datetime'] = format_datetime  # Register filter


# Initialize database
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                is_admin INTEGER DEFAULT 0
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS activity_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                activity TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        ''')

        # Ensure admin user exists
        cursor.execute("SELECT * FROM users WHERE username = 'admin'")
        admin_exists = cursor.fetchone()
        if not admin_exists:
            admin_password = generate_password_hash("admin")
            cursor.execute("INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)", 
                           ('admin', admin_password, 1))
        
        conn.commit()

# Log user activity
def log_activity(user_id, activity):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO activity_log (user_id, activity) VALUES (?, ?)", (user_id, activity))
        conn.commit()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        try:
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
                flash("Registration successful! Please log in.")
                return redirect(url_for('home'))
        except sqlite3.IntegrityError:
            flash("Username already exists.")
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['is_admin'] = user[3]

            log_activity(user[0], "Logged in")

            return redirect(url_for('admin' if user[3] else 'profile'))

    flash("Invalid username or password.")
    return redirect(url_for('home'))

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('home'))
    log_activity(session['user_id'], "Viewed profile")
    return render_template('profile.html', username=session['username'], user_id=session['user_id'])

@app.route('/attend')
def attend():
    if 'user_id' not in session:
        return redirect(url_for('home'))
    log_activity(session['user_id'], "Class Attended")
    return render_template('profile.html', username=session['username'])

@app.route('/admin')
def admin():
    if 'is_admin' in session and session['is_admin']:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, username FROM users")
            users = cursor.fetchall()
        return render_template('admin.html', users=users)
    return redirect(url_for('home'))

@app.route('/activity_log')
def activity_log():
    if 'user_id' not in session:
        flash("Please log in to access activity logs.")
        return redirect(url_for('home'))

    with sqlite3.connect(DATABASE) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        if session.get('is_admin'):
            cursor.execute('''
                SELECT a.id, u.username, a.activity, a.timestamp
                FROM activity_log a
                LEFT JOIN users u ON a.user_id = u.id
                ORDER BY a.timestamp DESC
            ''')
        else:
            cursor.execute('''
                SELECT id, activity, timestamp FROM activity_log 
                WHERE user_id = ? ORDER BY timestamp DESC
            ''', (session['user_id'],))

        logs = cursor.fetchall()

    return render_template('activity_log.html', logs=logs)

# Duration calculation
def durc(start, end):
    if not start or not end:
        return "N/A"
    start_dt = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    end_dt = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    return end_dt - start_dt

# Fetch timestamps helper function
def fetch_timestamps(cursor, user_id, activity):
    try:
        cursor.execute("""
            SELECT MIN(timestamp), MAX(timestamp)
            FROM activity_log 
            WHERE user_id = ? AND activity = ?
        """, (user_id, activity))
        return cursor.fetchone()
    except Exception as e:
        print(f"Error fetching timestamps: {e}")
        return None, None

@app.route('/sessionview/<int:id>')
def sessionview(id):
    if 'user_id' not in session:
        return redirect(url_for('home'))
    if not session.get('is_admin') and session['user_id'] != id:
        flash("Access Denied")
        return redirect(url_for('profile'))

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()

        # Fetch activity logs
        cursor.execute("SELECT activity, timestamp FROM activity_log WHERE user_id = ? ORDER BY timestamp DESC", (id,))
        logs = cursor.fetchall()

        # Fetch timestamps for different activities
        active_start, active_end = fetch_timestamps(cursor, id, "Active")
        distracted_start, distracted_end = fetch_timestamps(cursor, id, "Distracted")
        asleep_start, asleep_end = fetch_timestamps(cursor, id, "Asleep")
        look_away_start, look_away_end = fetch_timestamps(cursor, id, "Look Away")

        # Calculate durations
        at = durc(active_start, active_end)
        dt = durc(distracted_start, distracted_end)
        ast = durc(asleep_start, asleep_end)
        lat = durc(look_away_start, look_away_end)

    return render_template('sessionview.html', logs=logs, at=at, dt=dt, ast=ast, lat=lat)

@app.route('/logout')
def logout():
    if 'user_id' in session:
        log_activity(session['user_id'], "Logged out")
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
