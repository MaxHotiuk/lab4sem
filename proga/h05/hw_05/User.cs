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
    }
}