using System;
namespace Algorithms.CodeChallenges
{
    /***
    * Given strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character
    * S="ab#c", T="ad#c", true because both return "ac"
    * S="ab##", T="c#d#", true because return ""
    * S="ab##c", T="#a#c" return true because both return "c"
    * S="a#c", T="b" return false, because S="c" and T="b"
    * 1 <= S.length <= 200 | 1 <= T.length <= 200 > S and T only contain lowercase letters and '#' characters.
    * Solve in O(n) time and O(1) space
    ***/
    public static class BackspaceStringCompare
    {
        public static void Execute(){
            Console.WriteLine($"Factorial of 5 is: {backspaceCompare("ab#c","ad#c")}");
            Console.WriteLine($"Factorial of 5 (recursive) is: {backspaceCompare("ab##", "c#d#")}");
        }

        private static bool backspaceCompare(string S, string T) {
            return true;
        }
    }
}