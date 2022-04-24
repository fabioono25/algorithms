namespace Algorithms.CodeChallenges
{
    /***
    * verify if the array contains any duplicates
    * [1,2,3,1] true
    * [1,2,3,4] false
    ***/
    public static class ContainsDuplicates
    {
        public static void Execute(){
            Console.WriteLine($"[1,2,3,1] contains duplicates: {containsDuplicates(new[] {1,2,3,1})}");
            Console.WriteLine($"[1,2,3,4] contains duplicates: {containsDuplicates(new[] {1,2,3,4})}");            
        }

        // considering that the input strings are same length, otherwise we should verify and return false if they are different
        private static bool containsDuplicates(int[] items) {

            var distinct = new HashSet<int>();

            foreach(var item in items) {
                if (!distinct.Add(item)) {
                    return true;
                }
            }

            return false;
        }
    }
}