public class Palindrome{
	public static void main(String args[])
	{
		int num = 456, rev = 0, original = num;

		for(;num > 0; num /= 10){
			rev = rev * 10 + num % 10;
		}

		if(original == rev){
			System.out.println(original + "is a palindrome.");
		}else{
			System.out.println(original + "is not a palindrome");
		}
	}
}