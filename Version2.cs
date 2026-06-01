// a Average Version :D


using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Main
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double number1;
            double number2;
            double number3;

            Console.Title = " Average Calculator in C#";
            Console.Write("Enter Your First Mumber");
            number1 = Convert.ToDouble(Console.ReadLine() );
            Console.Write("Enter Your Second Number");
            number2 = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter your Thrid Number");
            number3 = Convert.ToDouble(Console.ReadLine());
            double result = number1 / number2 / number3;
            Console.WriteLine("the Average is :" + result);
            Console.ReadKey();

        }
    }
}
