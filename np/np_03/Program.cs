using System;
using System.Collections.Generic;
using System.IO;

// Клас БУДИНОК
public class House : IComparable<House>
{
    public string StreetName { get; set; }
    public int HouseNumber { get; set; }
    public double LivingArea { get; set; }

    public House(string streetName, int houseNumber, double livingArea)
    {
        StreetName = streetName;
        HouseNumber = houseNumber;
        LivingArea = livingArea;
    }

    public int CompareTo(House other)
    {
        return string.Compare(StreetName, other.StreetName, StringComparison.Ordinal);
    }

    public override string ToString()
    {
        return $"{StreetName}, {HouseNumber}, {LivingArea} m²";
    }

    public override bool Equals(object obj)
    {
        if (obj is House house)
        {
            return StreetName == house.StreetName && HouseNumber == house.HouseNumber && LivingArea == house.LivingArea;
        }
        return false;
    }

    public override int GetHashCode()
    {
        return HashCode.Combine(StreetName, HouseNumber, LivingArea);
    }
}

// Клас-колекція БУДИНКІВ
public class HouseCollection : IEnumerable<House>
{
    private List<House> houses = new List<House>();

    public void Add(House house)
    {
        houses.Add(house);
    }

    public void SortByStreetName()
    {
        houses.Sort();
    }

    public void SortByHouseNumber()
    {
        houses.Sort((h1, h2) => h1.HouseNumber.CompareTo(h2.HouseNumber));
    }

    public void SortByLivingArea()
    {
        houses.Sort((h1, h2) => h1.LivingArea.CompareTo(h2.LivingArea));
    }

    public House FindByStreetAndNumber(string streetName, int houseNumber)
    {
        return houses.Find(h => h.StreetName == streetName && h.HouseNumber == houseNumber);
    }

    public IEnumerator<House> GetEnumerator()
    {
        return houses.GetEnumerator();
    }

    System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }

    public static HouseCollection LoadFromFile(string filePath)
    {
        HouseCollection collection = new HouseCollection();
        using (StreamReader reader = new StreamReader(filePath))
        {
            string line;
            while ((line = reader.ReadLine()) != null)
            {
                string[] parts = line.Split(',');
                if (parts.Length == 3)
                {
                    string streetName = parts[0].Trim();
                    int houseNumber = int.Parse(parts[1].Trim());
                    double livingArea = double.Parse(parts[2].Trim());
                    collection.Add(new House(streetName, houseNumber, livingArea));
                }
            }
        }
        return collection;
    }
}

// Завантажити дані з файлу
HouseCollection houses = HouseCollection.LoadFromFile("houses.txt");

// Вивести всі будинки
foreach (House house in houses)
{
    Console.WriteLine(house);
}

// Відсортувати за назвою вулиці
houses.SortByStreetName();
Console.WriteLine("\nВідсортовано за назвою вулиці:");
foreach (House house in houses)
{
    Console.WriteLine(house);
}

// Знайти будинок за назвою вулиці та номером
House foundHouse = houses.FindByStreetAndNumber("Вулиця Шевченка", 25);
if (foundHouse != null)
{
    Console.WriteLine($"\nЗнайдено будинок: {foundHouse}");
}
else
{
    Console.WriteLine("\nНе знайдено будинок за заданими критеріями.");
}