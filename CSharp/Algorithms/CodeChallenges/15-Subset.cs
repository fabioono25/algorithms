namespace Algorithms.CodeChallenges
{
    /***
    * Given two arrays, verify if one of them is a subset of another
    * Ex: ['a','b','c','d','e','f','g']. ['a','d','g'] is a subset
    * Ex: ['a','b','c','d','e','f','g']. ['a','z','g'] is not a subset
    ***/
    public static class Subset
    {
        public static void Execute(){
            Console.WriteLine($"['a','d','g'] is a subset of ['a','b','c','d','e','f','g']: {subset(new[] {'a','b','c','d','e','f','g'}, new[] {'a','d','g'})}");
            Console.WriteLine($"['a','z','g'] is a subset of ['a','b','c','d','e','f','g']: {subset(new[] {'a','b','c','d','e','f','g'}, new[] {'a','z','g'})}");
        }

        private static bool subset(char[] A, char[] B) {

            var largestArray = A;
            var smallerArray = B;
            // who is the subset
            if (B.Length < A.Length) {
                largestArray = A;
                smallerArray = B;
            }

            // now, instead of avoiding one loop inside another O(n * m)
            // we will focus on adding in a dictionary (hashtable), turning the operation in O(n)
            var dict = new Dictionary<char, bool>();
            foreach (var item in A)
            {
                dict.Add(item, true);
            }

            // here is the time to run through the subset and verify based on the hashtable (dict, hashmap)
            foreach (var item in B){
                if (!dict.ContainsKey(item)){
                    return false;
                }
            }

            return true;
        }
    }
}