using System;
using System.Collections.Generic;

class Program
{
    static void Main() {
        List<int> numbers = new List<int>();  
        int input;

        Console.WriteLine("Enter a list of numbers, type 0 when finished.");
        do {
            Console.Write("Enter number: ");
            input = int.Parse(Console.ReadLine());

            if (input != 0) {
                numbers.Add(input);
            }

        } while (input != 0);

        int sum = 0;
        foreach (int number in numbers) {
            sum += number;
        }

        double average = (double)sum / numbers.Count;

        int largest = int.MinValue;
        foreach (int number in numbers) {
            if (number > largest)  {
                largest = number;
            }
        }

        Console.WriteLine($"The sum is: {sum}");
        Console.WriteLine($"The average is: {average}");
        Console.WriteLine($"The largest number is: {largest}");

        // Stretch Challenge 1
        int smallestPositive = int.MaxValue;
        foreach (int number in numbers) {
            if (number > 0 && number < smallestPositive) {
                smallestPositive = number;
            }
        }
        Console.WriteLine($"The smallest positive number is: {smallestPositive}");  

        // Stretch Challenge 2
        numbers.Sort();  
        Console.WriteLine("The sorted list is:");  
        foreach (int number in numbers) {
            Console.WriteLine(number);
        }
    }
}
