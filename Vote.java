public class Vote{
	static public void main(String args[])
	{
		int person = 18;
		if(person>=18)
		{
			System.out.println("Person is eligible to vote:" + person);

		}else{
			if(person<=18)
			{
				System.out.println("Person is not eligible to vote:" + person);
			}
		}
	}
}