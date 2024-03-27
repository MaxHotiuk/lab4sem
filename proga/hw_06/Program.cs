namespace hw_06;

class Program
{
    static List<Order<Electronics>> electronicsOrders = new List<Order<Electronics>>();
    static List<Order<Clothing>> clothingOrders = new List<Order<Clothing>>();

    static void Main(string[] args)
    {
        bool exit = false;
        while (!exit)
        {
            Console.WriteLine("Меню:");
            Console.WriteLine("1. Додати нове замовлення для електроніки");
            Console.WriteLine("2. Додати нове замовлення для одягу");
            Console.WriteLine("3. Переглянути замовлення для електроніки");
            Console.WriteLine("4. Переглянути замовлення для одягу");
            Console.WriteLine("5. Сума цін товарів у замовленнях");
            Console.WriteLine("6. Вихід");
            Console.Write("Виберіть опцію: ");

            int choice = int.Parse(Console.ReadLine());

            switch (choice)
            {
                case 1:
                    AddElectronicsOrder();
                    break;
                case 2:
                    AddClothingOrder();
                    break;
                case 3:
                    PrintElectronicsOrders();
                    break;
                case 4:
                    PrintClothingOrders();
                    break;
                case 5:
                    Console.WriteLine($"Сума цін товарів у замовленнях: {electronicsOrders.Sum(order => order.CalculateTotal()) + clothingOrders.Sum(order => order.CalculateTotal())}");
                    break;
                case 6:
                    exit = true;
                    break;
                default:
                    Console.WriteLine("Некоректний вибір. Спробуйте ще раз.");
                    break;
            }

            Console.WriteLine();
        }
    }

    static void AddElectronicsOrder()
    {
        Order<Electronics> order = new Order<Electronics>();
        Console.Write("Введіть кількість товарів для замовлення: ");
        int itemCount = int.Parse(Console.ReadLine());

        for (int i = 0; i < itemCount; i++)
        {
            Console.Write($"Введіть назву товару #{i + 1}: ");
            string name = Console.ReadLine();
            Console.Write($"Введіть ціну товару #{i + 1}: ");
            double price = double.Parse(Console.ReadLine());
            Console.Write($"Введіть кількість товару #{i + 1}: ");
            int quantity = int.Parse(Console.ReadLine());
            Console.Write($"Введіть виробника товару #{i + 1}: ");
            string manufacturer = Console.ReadLine();
            Console.Write($"Введіть модель товару #{i + 1}: ");
            string model = Console.ReadLine();

            order.AddItem(new Product<Electronics>(name, price, quantity, new Electronics { Manufacturer = manufacturer, Model = model }));
        }

        electronicsOrders.Add(order);
        Console.WriteLine("Замовлення для електроніки додано успішно.");
    }

    static void AddClothingOrder()
    {
        Order<Clothing> order = new Order<Clothing>();
        Console.Write("Введіть кількість товарів для замовлення: ");
        int itemCount = int.Parse(Console.ReadLine());

        for (int i = 0; i < itemCount; i++)
        {
            Console.Write($"Введіть назву товару #{i + 1}: ");
            string name = Console.ReadLine();
            Console.Write($"Введіть ціну товару #{i + 1}: ");
            double price = double.Parse(Console.ReadLine());
            Console.Write($"Введіть кількість товару #{i + 1}: ");
            int quantity = int.Parse(Console.ReadLine());
            Console.Write($"Введіть розмір товару #{i + 1}: ");
            string size = Console.ReadLine();
            Console.Write($"Введіть колір товару #{i + 1}: ");
            string color = Console.ReadLine();

            order.AddItem(new Product<Clothing>(name, price, quantity, new Clothing { Size = size, Color = color }));
        }

        clothingOrders.Add(order);
        Console.WriteLine("Замовлення для одягу додано успішно.");
    }

    static void PrintElectronicsOrders()
    {
        if (electronicsOrders.Count == 0)
        {
            Console.WriteLine("Немає замовлень для електроніки.");
        }
        else
        {
            Console.WriteLine("Замовлення для електроніки:");
            for (int i = 0; i < electronicsOrders.Count; i++)
            {
                Console.WriteLine($"Замовлення #{i + 1}:");
                electronicsOrders[i].DisplayOrder();
                Console.WriteLine();
            }
        }
    }

    static void PrintClothingOrders()
    {
        if (clothingOrders.Count == 0)
        {
            Console.WriteLine("Немає замовлень для одягу.");
        }
        else
        {
            Console.WriteLine("Замовлення для одягу:");
            for (int i = 0; i < clothingOrders.Count; i++)
            {
                Console.WriteLine($"Замовлення #{i + 1}:");
                clothingOrders[i].DisplayOrder();
                Console.WriteLine();
            }
        }
    }
}