using System.Collections.Generic;
namespace Algorithms.CodeChallenges
{
    /***
    * Calculate a Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    * F(n) = F(n-1) + F(n-2)
    * calculate Fibonacci for a term number = n (length) >= 0
    ***/
    public static class Fibonacci
    {
        public static void Execute(){
            // O(n)
            Console.WriteLine($"Fibonacci of 1 is: {fibonacci(1)}");
            Console.WriteLine($"Fibonacci of 2 is: {fibonacci(2)}"); 
            Console.WriteLine($"Fibonacci of 7 is: {fibonacci(7)}");
            Console.WriteLine($"Fibonacci of 9 is: {fibonacci(9)}");

            // O(n)
            Console.WriteLine($"Fibonacci of 1 using array is: {fibonacciWithArray(1)}");
            Console.WriteLine($"Fibonacci of 2 using array is: {fibonacciWithArray(2)}");            
            Console.WriteLine($"Fibonacci of 7 using array is: {fibonacciWithArray(7)}");
            Console.WriteLine($"Fibonacci of 9 using array is: {fibonacciWithArray(9)}");

            // O(2^n)
            Console.WriteLine($"Fibonacci [recursive] of 1 is: {fibonacciRecursive(1)}");
            Console.WriteLine($"Fibonacci [recursive] of 2 is: {fibonacciRecursive(2)}");
            Console.WriteLine($"Fibonacci [recursive] of 7 is: {fibonacciRecursive(7)}");
            Console.WriteLine($"Fibonacci [recursive] of 9 is: {fibonacciRecursive(9)}");

            // O(n)
            Console.WriteLine($"Fibonacci [recursive with memoization] of 1 is: {fibonacciCache(1)}");
            Console.WriteLine($"Fibonacci [recursive with memoization] of 2 is: {fibonacciCache(2)}");
            Console.WriteLine($"Fibonacci [recursive with memoization] of 7 is: {fibonacciCache(7)}");
            Console.WriteLine($"Fibonacci [recursive with memoization] of 9 is: {fibonacciCache(9)}");

            // O(n)
            Console.WriteLine($"Fibonacci [with stack] of 1 is: {fibonacciStack(1)}");
            Console.WriteLine($"Fibonacci [with stack] of 2 is: {fibonacciStack(2)}");
            Console.WriteLine($"Fibonacci [with stack] of 7 is: {fibonacciStack(7)}");
            Console.WriteLine($"Fibonacci [with stack] of 9 is: {fibonacciStack(9)}");
        }

        // O(n)
        private static int fibonacci(int n) {
            if (n < 2)
                return n;

            var first = 0;
            var second = 1;
            var result = 0;
            for (int i = 2; i <= n; i++)
            {
                result = first + second;
                first = second;
                second = result;
            }

            return result;
        }

        // O(n)
        private static int fibonacciWithArray(int n) {
            if (n < 2)
                return n;
            
            var ret = new int[n+1];
            ret[0] = 0;
            ret[1] = 1;

            var i = 2;
            for (; i < n + 1; i++)
                ret[i] = ret[i-2] + ret[i-1];
                
            return ret[i-1];
        }

        // O(2^N)
        private static int fibonacciRecursive(int n) {
            if (n < 2)
                return n;

            return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
        }

        // O(N)
        private static readonly Dictionary<int, long> cache = new() {{0,0}, {1,1}};
        private static long fibonacciCache(int n) {

            if (cache.ContainsKey(n))
                return cache[n];

            var val = fibonacciCache(n - 1) + fibonacciCache(n - 2);
            cache[n] = val;

            return val;
        }

        // Fibonacci using stack (bottom-up)
        private static long fibonacciStack(int n)
        {
            var result = new Stack<int>();
            result.Push(0);
            result.Push(1);
            for (int i = 2; i <= n; i++)
            {
                var current = result.Pop();
                var previous = result.Pop();
                var next = previous + current;
                result.Push(previous);
                result.Push(current);
                result.Push(next);
            }
            return result.Pop();
        }
    }
}