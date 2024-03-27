namespace proga.hw_05
{
    public class ShoppingCart
    {
        private List<Product> products = new List<Product>();

        public delegate void CartChangedEventHandler(object source, EventArgs args);
        public event CartChangedEventHandler? ProductAdded;
        public event CartChangedEventHandler? ProductRemoved;

        protected virtual void OnProductAdded()
        {
            ProductAdded?.Invoke(this, EventArgs.Empty);
        }

        protected virtual void OnProductRemoved()
        {
            ProductRemoved?.Invoke(this, EventArgs.Empty);
        }

        public void AddProduct(Product product)
        {
            products.Add(product);
            OnProductAdded();
        }

        public void RemoveProduct(Product product)
        {
            products.Remove(product);
            OnProductRemoved();
        }

        public void SortByPrice()
        {
            products = products.OrderBy(p => p.Price).ToList();
        }

        public void SortByRating()
        {
            products = products.OrderByDescending(p => p.Rating).ToList();
        }

        public double CalculateTotalPrice()
        {
            double totalPrice = 0;
            foreach (Product product in products)
            {
                totalPrice += product.Price;
            }
            return totalPrice;
        }

        public void PrintCart()
        {
            Console.WriteLine("Shopping Cart:");
            foreach (var product in products)
            {
                Console.WriteLine($"Name: {product.Name}, Price: {product.Price}, Rating: {product.Rating}");
            }
        }

    }       
}