namespace Algorithms.CodeChallenges
{
    /***
    * Factorial is defined for n! = n X (n - 1) x (n - 2) x (n - 3) = n x (n - 1)!
    * 5! = 5 * 4 * 3 * 2 * 1 = 5 * 24 = 120
    ***/
    public static class Factorial
    {
        public static void Execute(){
            Console.WriteLine($"Factorial of 25 is: {factorial(25)}");
            Console.WriteLine($"Factorial of 5 is: {factorial(5)}");
            Console.WriteLine($"Factorial of 2 is: {factorial(2)}");
            Console.WriteLine($"Factorial of 1 is: {factorial(1)}");
            Console.WriteLine($"Factorial of 25 (recursive) is: {factorialRecursive(25)}");
            Console.WriteLine($"Factorial of 5 (recursive) is: {factorialRecursive(5)}");
            Console.WriteLine($"Factorial of 2 (recursive) is: {factorialRecursive(2)}");
            Console.WriteLine($"Factorial of 1 (recursive) is: {factorialRecursive(1)}");
        }

        private static int factorial(int n) {
            var result = n;
            for (var i = n; i > 2; i--)
                result *= (i-1);

            return result;
        }

        private static int factorialRecursive(int n) {
            if (n < 2)
                return 1;

            return n * factorialRecursive(n - 1);
        }
    }
}