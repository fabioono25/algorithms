namespace Algorithms.CodeChallenges
{
    /***
    * Returning a string reversed based on the input
    ***/
    public static class ReverseString
    {
        public static void Execute(){
            Console.WriteLine(reverse("a"));
            Console.WriteLine(reverse("hello, how are you?"));
        }

        private static string reverse(string s) {
            var result = string.Empty;
            for (int i = s.Length-1; i >= 0; i--){
                result += s[i];
            }
            return result;
        }
    }
}