 using System;
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
            int number1;
            int number2;

            Console.Title = "Simple Calculator in C#";
            Console.Write("Input a Number: ");

            number1 = Convert.ToInt32( Console.ReadLine());
            Console.Write("input a 2nd number: ");
            number2 = Convert.ToInt32(Console.ReadLine());

            int result = number1 * number2;
            Console.WriteLine("it is " + result);

            Console.ReadKey();

        }
    }
}