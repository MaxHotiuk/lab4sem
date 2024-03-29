namespace hw_06;

class Product<T>
{
    public string Name { get; set; }
    public double Price { get; set; }
    public int Quantity { get; set; }
    public T ProductDetails { get; set; }

    public Product(string name, double price, int quantity, T productDetails)
    {
        Name = name;
        Price = price;
        Quantity = quantity;
        ProductDetails = productDetails;
    }
}

// Класи для різних категорій товарів
class Electronics
{
    public string Manufacturer { get; set; }
    public string Model { get; set; }
}

class Clothing
{
    public string Size { get; set; }
    public string Color { get; set; }
}

class Book
{
    public string Author { get; set; }
    public string Genre { get; set; }
}

class Food
{
    public DateTime ExpirationDate { get; set; }
}