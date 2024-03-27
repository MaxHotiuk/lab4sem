namespace proga.hw_05
{
    public class Product
    {
        public string Name { get; set; }
        public double Price { get; set; }
        public double Rating { get; set; }

        public Product(string name, double price, int rating)
        {
            Name = name;
            Price = price;
            Rating = rating;
        }
    }
}