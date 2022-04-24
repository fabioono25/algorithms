namespace Algorithms.CodeChallenges
{
    /***
    * verify if a string is an anagram or not
    * anagram and nararam are anagrams
    * rat and car are not anagrams
    ***/
    public static class Anagram
    {
        public static void Execute(){
            Console.WriteLine($"Are anagram and nagaram anagrams? {anagram("anagram", "nagaram")}");
            Console.WriteLine($"Are rat and car anagrams? {anagram("rat", "car")}");
        }

        // considering that the input strings are same length, otherwise we should verify and return false if they are different
        private static bool anagram(string s1, string s2) {
            var dict = new Dictionary<char, int>();
            var arr = new String[s1.Length];

            foreach(var c in s1){
                if (!dict.ContainsKey(c)){
                    dict[c] = 1;
                    continue;
                }
                dict[c]+=1;
            }

            foreach(var c in s2){
                if (dict.ContainsKey(c)){
                    dict[c] -= 1;
                }
            }

            return dict.Any(d => d.Value > 0);
        }
    }
}