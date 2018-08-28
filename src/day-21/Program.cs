using System;
using System.Collections.Generic;

namespace day_21
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create a new List with initial Fibonacci values
            var fibonacci = new List<int> { 1, 1 };

            // Get the first 20 values of the sequence
            while (fibonacci.Count < 20)
            {
                // Count the items in the List then -1 for the last digit and -2 for next to last number
                var previousNumber = fibonacci[fibonacci.Count - 1];
                var previousNumber2 = fibonacci[fibonacci.Count - 2];

                // Add the sum of the last two numbers to the List with .Add
                fibonacci.Add(previousNumber + previousNumber2);

                // Print each number of the sequence to the console
                foreach (var number in fibonacci)
                {
                    Console.Write($"{number}, ");
                }
                // Move the cursor onto a new line for the next iteration 
                Console.WriteLine();
            }
            
            Console.WriteLine("Press any key to exit...");
            // Keeps the console open until a key is pressed to exit
            Console.ReadKey();
        }
    }
}
