namespace hw_06;
class Order<T> : IOrder<T>
{
    private List<Product<T>> items = new List<Product<T>>();

    public void AddItem(Product<T> item)
    {
        items.Add(item);
    }

    public double CalculateTotal()
    {
        double total = 0;
        foreach (var item in items)
        {
            total += item.Price * item.Quantity;
        }
        return total;
    }

    public void DisplayOrder()
    {
        Console.WriteLine("Деталі замовлення:");
        foreach (var item in items)
        {
            Console.WriteLine($"Назва: {item.Name}, Ціна: {item.Price}, Кількість: {item.Quantity}");
        }
        Console.WriteLine($"Загальна сума: {CalculateTotal()}");
    }
}