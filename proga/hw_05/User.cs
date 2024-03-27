namespace proga.hw_05
{
    public class User
    {
        public string Name { get; set; }
        public string Type { get; set; }

        public User(string name, string type)
        {
            Name = name;
            Type = type;
        }
        
        public double CalculateDiscount(int quantity)
        {
            double discount = 0;
            if (quantity > 10)
            {
                discount += 0.05;
            }

            if (Type == "Premium")
            {
                discount += 0.1;
            }

            return discount;
        }
    }
}