namespace proga.hw_05;
public class Program
{
    public delegate double DiscountDelegate(int quantity, string userType);

    public static void Main()
    {
        DiscountDelegate discountCalc = CalculateDiscount;
        User user = new User("John", "Premium");
        double discount = discountCalc(15, user.Type);
        Console.WriteLine($"Discount: {discount}%");
        ShoppingCart cart = new ShoppingCart();

        Product product1 = new Product("Laptop", 1000, 5);
        Product product2 = new Product("Phone", 500, 4);
        Product product3 = new Product("Tablet", 300, 3);
        Product product4 = new Product("Smartwatch", 200, 2);

        cart.ProductAdded += (source, args) => Console.WriteLine("Product added to cart");
        cart.AddProduct(product1);
        cart.AddProduct(product2);
        cart.AddProduct(product3);
        cart.AddProduct(product4);

        cart.ProductRemoved += (source, args) => Console.WriteLine("Product removed from cart");
        cart.RemoveProduct(product2);
        
        cart.SortByPrice();
        cart.PrintCart();
        cart.SortByRating();
        cart.PrintCart();
    }

    public static double CalculateDiscount(int quantity, string userType)
    {
        double discount = 0;
        if (quantity > 10)
        {
            discount += 5;
        }

        if (userType == "Premium")
        {
            discount += 10;
        }

        return discount;
    }
}