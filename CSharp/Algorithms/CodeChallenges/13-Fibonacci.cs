namespace Algorithms.CodeChallenges
{
    /***
    * Calculate a Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    * F(n) = F(n-1) + F(n-2)
    * calculate Fibonacci for a term number = n (length)
    ***/
    public static class Fibonacci
    {
        public static void Execute(){
            Console.WriteLine($"Fibonacci of 1 is: {fibonacci(1)}");
            Console.WriteLine($"Fibonacci of 7 is: {fibonacci(7)}");
            Console.WriteLine($"Fibonacci of 9 is: {fibonacci(9)}");

            Console.WriteLine($"Fibonacci [recursive] of 1 is: {fibonacci(1)}");
            Console.WriteLine($"Fibonacci [recursive] of 7 is: {fibonacci(7)}");
            Console.WriteLine($"Fibonacci [recursive] of 9 is: {fibonacci(9)}");            
        }

        private static int fibonacci(int n) {
            if (n == 0 || n == 1)
                return n;
            
            var first = 0;
            var second = 1;
            var result = 0;
            for (int i = 2; i < n; i++)
            {
                result = first + second;
                first = second;
                second = result;
            }

            return result;
        }

        private static int fibonacciRecursive(int n) {
            if (n == 0 || n == 1)
                return n;

            return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
        }
    }
}