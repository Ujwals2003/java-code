public class ProductDetails{
	public static void main(String args[])
	{
		System.out.println("THE PRODUCR DETAILS ARE:");
		String productName = "Mobile Phone";
		String brandName = "apple";
		float price = 700000f;
		float discount = 20;
		float deliveryFee = 100f;
		float platformFee = 40f;
		float donation = 60f;
		float gst = 20f;
		float sum = price+discount+deliveryFee+platformFee+donation+gst;
		float sub = sum-gst;
		float discountAmount =(price * (discount/100));
		float gstAmount = (price * (gst/100));
		System.out.println("the product Name is" + productName);
		System.out.println("the brand name is" + brandName);
		System.out.println("the price of the product" + price);
		System.out.println("the discount is" + discount + "%");
		System.out.println("the deliveryFee is" + deliveryFee);
		System.out.println("the platformFee is" + platformFee);
		System.out.println("the donation is" + donation );
		System.out.println("the GST is" + gst + "%");
		System.out.println("the disount amount is:" + discountAmount);
		System.out.println("the gst amount is:" + gstAmount);
		System.out.println("THE TOTAL AMOUNT IS");
		System.out.println("Sum:" + sum);
		System.out.println("THE TOTAL PAYABLE AMOUNT IS"+ (sum - discountAmount));
		System.out.println("THE TOTAL AMOUNT WITHOUT GST:" + sub);



	}
}