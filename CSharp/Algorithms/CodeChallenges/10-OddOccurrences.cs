namespace Algorithms.CodeChallenges
{
    /***
    * one array [9,3,9,3,9,7,9] has 7 as unpaired element
    ***/
    public static class OddOccurrences
    {
        public static void Execute(){
            Console.WriteLine($"The [3, 8, 9, 7, 6] by K=1 will give: {findOdd(new[]{9,3,9,3,9,7,9})}");            
        }

        private static int findOdd(int[] items) {
            var set = new HashSet<int>();

            for (int i=0; i < items.Length; i++) {
                if (set.Contains(items[i]))
                    set.Remove(items[i]);
                else
                    set.Add(items[i]);
            }

            return set.Single();
        }
    }
}