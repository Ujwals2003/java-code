public class StaticExample {
    static String name = "UJWAL S";
    static int age = 21;
    static float height = 4.5f;
    static double weight = 55.5;
    static boolean isEmployed = true;
    static boolean hasLicense = false;
    static char grade = 'A';
    static String city = "CHIKKAMAGALURU";
    static String country = "INDIA";
    static int experience = 2;
    static double salary = 500000.0;
    static int numLanguages = 3;
    static boolean isStudent = false;
    static boolean ownVehicle = true;
    static String bloodGroup = "O+";

    public static void main(String args[]) {
        System.out.println("The details of the Person:\n");

        if (age >= 18) {
            System.out.println(name + " is an adult. Age: " + age);
        }

        if (height > 6.0) {
            System.out.println(name + " is tall. Height: " + height);
        } else {
            System.out.println(name + " is not tall. Height: " + height);
        }

        if (isEmployed) {
            System.out.println(name + " is employed.");
        } else {
            System.out.println(name + " is not employed.");
        }

        if (hasLicense) {
            System.out.println(name + " has a driving license.");
        } else {
            System.out.println(name + " does not have a driving license.");
        }

        if (weight < 50) {
            System.out.println(name + " is underweight. Weight: " + weight);
        } else if (weight >= 50 && weight <= 80) {
            System.out.println(name + " has a normal weight. Weight: " + weight);
        } else {
            System.out.println(name + " is overweight. Weight: " + weight);
        }

        if (city.equals("CHIKKAMAGALURU")) {
            System.out.println(name + " lives in Chikkamagaluru.");
        } else {
            System.out.println(name + " lives in a different city.");
        }

        if (country.equals("INDIA")) {
            System.out.println(name + " is from India.");
        } else {
            System.out.println(name + " is from another country.");
        }

        if (experience > 5) {
            System.out.println(name + " is an experienced professional with " + experience + " years of work.");
        } else {
            System.out.println(name + " is still gaining experience. Work experience: " + experience + " years.");
        }

        if (salary > 40000) {
            System.out.println(name + " earns a good salary of ₹" + salary);
        } else {
            System.out.println(name + " has a lower salary: ₹" + salary);
        }

        if (numLanguages >= 3) {
            System.out.println(name + " is multilingual and speaks " + numLanguages + " languages.");
        } else {
            System.out.println(name + " speaks only a few languages: " + numLanguages);
        }

        if (isStudent) {
            System.out.println(name + " is currently a student.");
        } else {
            System.out.println(name + " is not a student.");
        }

        if (ownVehicle) {
            System.out.println(name + " owns a vehicle.");
        } else {
            System.out.println(name + " does not own a vehicle.");
        }

        if (grade == 'A' || grade == 'B') {
            System.out.println(name + " has a good grade: " + grade);
        } else {
            System.out.println(name + " needs improvement. Grade: " + grade);
        }

        System.out.println(name + "'s blood group is " + bloodGroup + ".");
    }
}
