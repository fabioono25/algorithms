namespace Algorithms.CodeChallenges
{
    /***
    * in a string, find the first non-repeating character and return it's index. if it doesn't exist, return -1
    * leetcode = 0
    * loveleetcode = 2
    * aabbcc = -1
    ***/
    public static class FirstUniqueChar
    {
        public static void Execute(){
           Console.WriteLine($"First unique character of leetcode: {firsUniqueCharacterIndex("leetcode")}");
           Console.WriteLine($"First unique character of loveleetcode: {firsUniqueCharacterIndex("loveleetcode")}");
           Console.WriteLine($"First unique character of aabbcc: {firsUniqueCharacterIndex("aabbcc")}");
        }

        private static int firsUniqueCharacterIndex(string s) {
            var result = new Dictionary<char, int>();

            for (int i = 0; i < s.Length; i++)
            {
                if (result.ContainsKey(s[i]))
                    result[s[i]] = -1;
                else
                    result.Add(s[i], i);
            }

            return result.Any(r => r.Value != -1) ? result.First(r => r.Value != -1).Value : -1;
        }
    }
}