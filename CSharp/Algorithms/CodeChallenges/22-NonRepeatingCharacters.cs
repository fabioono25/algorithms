using static System.Net.WebRequestMethods;
using System.Collections.Generic;
using System.Net;
using System.Linq;

namespace Algorithms.CodeChallenges
{
    /***
    * given a string, find the first non-repeating character
    ***/
    public static class NonrepeatingCharacter
    {
        public static void Execute(){
            Console.WriteLine(NonrepeatingCharacterTest("hello world hi hey"));
        }

        public static string NonrepeatingCharacterTest(string str)
        {
            var dict = new Dictionary<char, int>();

            foreach (var x in str)
            {
                if (!dict.ContainsKey(x))
                    dict.Add(x, 1);
                else
                    dict[x] += 1;
            }

            return dict.First(d => d.Value == 1).Key.ToString();
        }
    }
}
