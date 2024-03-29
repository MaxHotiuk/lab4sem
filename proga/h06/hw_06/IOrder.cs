namespace hw_06;
interface IOrder<T>
{
    void AddItem(Product<T> item);
    double CalculateTotal();
    void DisplayOrder();
}