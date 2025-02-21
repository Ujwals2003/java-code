public class SwapNumbers{
	static public void main(String args[])
    {
        int n1 = 50, n2 = 4;
        System.out.println("THE N1 VALUES AND N2 VALUES IS:");
        System.out.println("BEFORE SWAPING");
        System.out.println("n1 ="+n1+",n2 =" + n2);
        n1 = n1 + n2;
        n2 = n1 - n2;
        n1 = n1 - n2;
       System.out.println("AFTER SWAPING");
        System.out.println("n1 ="+n1+",n2 =" + n2);
	}
}