public class Vehicle{
	public static void main(String args[])
	{
		int age = 5;
		if(age > 6 && age < 18)
		{
			System.out.println("you can ride a Bicycle but not Scooter and Car");

		}if(age >= 18)
		{
			System.out.println("you can ride a scoter and Car.");
		} 
		else{
			System.out.println("He is not eligible ");
		}
	}
}