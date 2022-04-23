namespace Algorithms.CodeChallenges
{
    /***
    * A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
    * Write a function: class Solution { public int solution(int N); }
    * that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
    * For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. 
    * Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
    * N is an integer within the range [1..2,147,483,647]
    ***/
    public static class BinaryGap
    {
        public static void Execute(){
            var entryValue = 1376796946;
            Console.WriteLine($"Entry value: {entryValue}");
            Console.WriteLine($"Longest Binary Gap: {solution(entryValue)}.");

            entryValue = 20;
            Console.WriteLine($"Entry value: {entryValue}");
            Console.WriteLine($"Longest Binary Gap: {solution(entryValue)}.");

            entryValue = 1041;
            Console.WriteLine($"Entry value: {entryValue}");
            Console.WriteLine($"Longest Binary Gap: {solution(entryValue)}.");

            entryValue = 32;
            Console.WriteLine($"Entry value: {entryValue}");
            Console.WriteLine($"Longest Binary Gap: {solution(entryValue)}.");
        }

        private static int solution(int n) {
            // convert the string value into binary
            var str = Convert.ToString(n, 2);

            // iterate to verify the pattern 1{n x 0s}1
            var started = false;
            var max = 0;
            var counter = 0;

            // avoid the fail in edge case 1000
            if (str.Count(x => x.Equals('1')) < 2)
                return 0;

            // extra treatment for last value
            str = str.Substring(0, str.LastIndexOf('1')+1);

            // interaction between values
            foreach (var c in str)
            {
                if (c.Equals('1')){
                    if (started && counter > max) {
                        max = counter;
                    }
                    counter = 0;
                    started = true;
                } else
                    counter++;
            }

            return max;
        }
    }
}