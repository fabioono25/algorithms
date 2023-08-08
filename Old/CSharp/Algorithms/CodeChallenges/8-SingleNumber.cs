namespace Algorithms.CodeChallenges
{
    /***
    * Given a non-empty array, there is a number that appears just once. Find this number
    * [2, 2, 1] = 1
    * [4, 1, 2, 1, 2] = 4
    * solve in linear runtime complexity without adding much space time complexity
    ***/
    public static class SingleNumber
    {
        public static void Execute(){
            Console.WriteLine($"Single number of [2, 2, 1] is: {string.Join(",", singleNumber(new []{2, 2, 1}))}");
            Console.WriteLine($"Single number of [4, 1, 2, 1, 2] is: {string.Join(",", singleNumber(new [] {4, 1, 2, 1, 2}))}");
            Console.WriteLine($"Single number of [2, 2, 1] is: {string.Join(",", singleNumber2(new []{2, 2, 1}))}");
            Console.WriteLine($"Single number of [4, 1, 2, 1, 2] is: {string.Join(",", singleNumber2(new [] {4, 1, 2, 1, 2}))}");
        }

        private static int singleNumber(int[] n) {
            var map = new HashSet<int>();
            foreach(var number in n) {
                if (map.Contains(number))
                    map.Remove(number);
                else
                    map.Add(number);
            }

            return map.Single();
        }

        private static int singleNumber2(int[] n) {
            var map = new HashSet<int>();
            foreach(var number in n) {
                if (!map.Add(number)) {
                    map.Remove(number);
                    continue;
                }
                map.Add(number);
            }

            return map.Single();
        }        
    }
}