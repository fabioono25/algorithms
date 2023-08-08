namespace Algorithms.CodeChallenges
{
    /***
    * Given a 32-bit signed integer, reverse digits of an integer
    * input: 123, output: 312 | input: -123, output: -321 | input: 120, output: 21
    ***/
    public static class ReverseInteger
    {
        public static void Execute(){
            Console.WriteLine($"Reverse integer 321: {reverse(321)}");
            Console.WriteLine($"Reverse integer 5: {reverse(5)}");
            Console.WriteLine($"Reverse integer -123: {reverse(-123)}");
            Console.WriteLine($"Reverse integer 120: {reverse(120)}");
            Console.WriteLine($"Reverse integer -120: {reverse(-120)}");
            Console.WriteLine($"Reverse integer 4321: {reverse(4321)}");
            Console.WriteLine($"Reverse V2 integer 321: {reverseV2(321)}");
            Console.WriteLine($"Reverse V2 integer 5: {reverseV2(5)}");
            Console.WriteLine($"Reverse V2 integer -123: {reverseV2(-123)}");
            Console.WriteLine($"Reverse V2 integer 120: {reverseV2(120)}");
            Console.WriteLine($"Reverse V2 integer -120: {reverseV2(-120)}");
            Console.WriteLine($"Reverse V2 integer 4321: {reverseV2(4321)}");
        }

        // TODO: there is space for more approaches here

        private static int reverse(int x) {
            var temporaryNumber = Math.Abs(x);
            var lengthOfNumber = temporaryNumber.ToString().Length - 1;

            int ret = 0;
            while (true)
            {
                if (temporaryNumber < 10)
                {
                    ret += temporaryNumber;
                    return ret * (x < 0 ? -1 : 1);
                }

                ret += (temporaryNumber % 10) * (int)Math.Pow(10, lengthOfNumber--);
                temporaryNumber /= 10;
            }
        }

        private static int reverseV2(int x)
        {
            var invertIfNegative = x < 0 ? -1 : 1; 

            int ret = 0;
            while (x > 0)
            {
                ret = (ret * 10) + (x % 10);
                x /= 10;
            }

            return ret * invertIfNegative;
        }
    }
}