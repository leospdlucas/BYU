using System;

class Program {
    // DisplayWelcome
    static void DisplayWelcome() {
        Console.WriteLine("Welcome to the Program!");
    }

    // PromptUserName
    static string PromptUserName() {
        Console.Write("Please enter your name: ");
        return Console.ReadLine();
    }

    // PromptUserNumber
    static int PromptUserNumber() {
        Console.Write("Please enter your favorite number: ");
        return int.Parse(Console.ReadLine());
    }

    // SquareNumber
    static int SquareNumber(int number) {
        return number * number;
    }

    // DisplayResult
    static void DisplayResult(string name, int squaredNumber) {
        Console.WriteLine($"{name}, the square of your number is {squaredNumber}");
    }

    static void Main() {
        DisplayWelcome();  

        string userName = PromptUserName();
        int userNumber = PromptUserNumber();

        int squaredNumber = SquareNumber(userNumber);

        DisplayResult(userName, squaredNumber);
    }
}
