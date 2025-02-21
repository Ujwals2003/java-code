public class Shopping{
	public static void main(String args[])
	{
		float prd1, prd2, prd3;
		prd1 = 6;
		prd2 = 8;
		prd3 = 100;
		 float total = prd1 + prd2 + prd3;
		System.out.println("The Total Cost of Product is:" + total);
		if(total > 100)
		{
			float discount = total - (total * 0.10f);
		
		System.out.println("Final Cost Is:" + discount);
	    }

	}
}