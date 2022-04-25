namespace Algorithms.CodeChallenges
{
    /***
    * Given an array of N elements, rotate the elements inside this array K times
    * [3, 8, 9, 7, 6] K=1 => [6, 3, 8, 9, 7]
    * [3, 8, 9, 7, 6] K=3 => [9, 7, 6, 3, 8]
    * [0, 0, 0] K=1 => [0, 0, 0]
    * [1, 2, 3, 4] K=4 => [1, 2, 3, 4]
    ***/
    public static class CyclicRotation
    {
        public static void Execute(){
            Console.WriteLine($"Rotate [3, 8, 9, 7, 6] by K=1 will give: {string.Join(",", rotate(new[]{3, 8, 9, 7, 6}, 1))}");
            Console.WriteLine($"Rotate [3, 8, 9, 7, 6] by K=3 will give: {string.Join(",", rotate(new[]{3, 8, 9, 7, 6}, 3))}");
            Console.WriteLine($"Rotate [0, 0, 0]  by K=1 will give: {string.Join(",", rotate(new[]{0, 0, 0}, 1))}");
            Console.WriteLine($"Rotate [1, 2, 3, 4] by K=4 will give: {string.Join(",", rotate(new[]{1, 2, 3, 4}, 4))}");
        }

        // considering that the input strings are same length, otherwise we should verify and return false if they are different
        private static int[] rotate(int[] items, int k) {

            // 1º we should correct k in order to avoid duplicated interactions
            var newK = k % items.Length;

            // 2º do nothing is k == len(array)
            if (newK == items.Length)
                return items;

            // 3º calculate
            var ret = new int[items.Length];

            for (int i = 0; i < items.Length; i++)
            {
                ret[(i+k)%items.Length] = items[i];
            }

            return ret;
        }
    }
}