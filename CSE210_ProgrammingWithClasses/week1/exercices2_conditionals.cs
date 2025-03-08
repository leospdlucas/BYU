using System;

class Program
{
    static void Main() {
        Console.Write("Enter your grade percentage: ");
        int grade = int.Parse(Console.ReadLine());

        string letter;  
        string sign = ""; 

        if (grade >= 90) {
            letter = "A";  
        }
        else if (grade >= 80) {
            letter = "B";  
        }
        else if (grade >= 70) {
            letter = "C"; 
        }
        else if (grade >= 60) {
            letter = "D";  
        }
        else {
            letter = "F";  
        }

        // Stretch Challenge 1
        if (letter != "F") {
            int lastNum = grade % 10;  
            if (lastNum >= 7) {
                sign = "+";  
            }
            else if (lastNum < 3) {
                sign = "-";  
            }
        }

        // Stretch Challenge 2
        if (letter == "A" && sign == "+") {
            sign = "-";  
        }

        // Stretch Challenge 3
        if (letter == "F") {
            sign = ""; 
        }

        Console.WriteLine($"Your grade is {letter}{sign}");

        if (grade >= 70) {
            Console.WriteLine("Congratulations, you passed the course!");
        }
        else {
            Console.WriteLine("Better luck next time!");
        }
    }
}