using System;

class Program
{
    static void Main() {
        Random random = new Random();  
        bool replay = true;  

        while (replay) {
            int randomNum = random.Next(1, 101);
            int guess = 0;
            int guessCount = 0;  
            bool correctNum = false;

            while (!correctNum) {
                Console.Write("What is your guess? ");
                guess = int.Parse(Console.ReadLine());
                guessCount++;  

                if (guess < randomNum) {
                    Console.WriteLine("Higher");
                }
                else if (guess > randomNum) {
                    Console.WriteLine("Lower");
                }
                else {
                    Console.WriteLine("You guessed it!");
                    correctNum = true;
                }
            }

            // Stretch Challenge 1
            Console.WriteLine($"It took you {guessCount} guesses.");

            // Stretch Challenge 2
            Console.Write("Do you want to play again? (yes/no): ");
            string response = Console.ReadLine().ToLower();
            if (response != "yes") {
                replay = false;
            }
        }
    }
}