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
            Console.WriteLine($"Is #ab equals ab?: {backspaceCompare("#ab", "ab")}");
            Console.WriteLine($"Is ab## equals c#d#?: {backspaceCompare("ab##", "c#d#")}");
            Console.WriteLine($"Is ab#c equals ad#c?: {backspaceCompare("ab#c", "ad#c")}");
            Console.WriteLine($"Is ab#c equals add#c?: {backspaceCompare("ab#c", "add#c")}");
            Console.WriteLine($"Is ab##c equals #a#c?: {backspaceCompare("ab##c", "#a#c")}");
            Console.WriteLine($"Is a#c equals b?: {backspaceCompare("a#c", "b")}");
        }

        private static bool backspaceCompare(string S, string T) {

            var sStack = new Stack<char>();
            var tStack = new Stack<char>();

            // O(N)
            foreach (var character in S)
                if (character != '#')
                    sStack.Push(character);
                else if (sStack.Count > 0)
                    sStack.Pop();

            foreach (var character in T)
            {
                if (character != '#')
                    tStack.Push(character);
                else if (tStack.Count > 0)
                    tStack.Pop();
            }

            // checking the stacks
            if (sStack.Count != tStack.Count)
                return false;

            while (sStack.Count != 0)
            {
                if (sStack.Pop() != tStack.Pop())
                    return false;
            }

            return true;
        }
    }
}