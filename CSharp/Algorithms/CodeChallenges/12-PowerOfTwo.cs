namespace Algorithms.CodeChallenges
{
    /***
    * given a number, write a function that determine if it is a power of two
    * 1 = true, 16 = true, 218 = false
    ***/
    public static class PowerOfTwo
    {
        public static void Execute(){
            Console.WriteLine($"Is 1 power of 2?: {isPowerOfTwo(1)}");
            Console.WriteLine($"Is 13 power of 2?: {isPowerOfTwo(13)}");
            Console.WriteLine($"Is 16 power of 2?: {isPowerOfTwo(16)}");
            Console.WriteLine($"Is 218 power of 2?: {isPowerOfTwo(218)}");
        }

        private static bool isPowerOfTwo(int n) {
            if (n == 1)
                return true;

            while (n > 1) {
                if (n % 2 != 0)
                    return false;
                n /= 2;
            }
            return true;

            // var i = 1;
            // while (i < n)
            // {
            //     i *= 2;
            // }

            // return i == n;
        }
    }
}