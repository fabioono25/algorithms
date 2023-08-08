using static System.Net.WebRequestMethods;
using System.Collections.Generic;
using System.Net;
using System.Linq;

namespace Algorithms.CodeChallenges
{
    /***
    * Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
    * If there is no such substring, return the empty string ""
    * The testcases will be generated such that the answer is unique.
    * A substring is a contiguous sequence of characters within the string.
    * Input: s = "ADOBECODEBANC", t = "ABC" - Output: "BANC" - Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t
    * Input: s = "a", t = "a" - Output: "a" - Explanation: The entire string s is the minimum window.
    * Input: s = "a", t = "aa" - Output: "" - Explanation: Both 'a's from t must be included in the window. - Since the largest window of s only has one 'a', return empty string.
    * m == s.length, n == t.length, 1 <= m, n <= 105, s and t consist of uppercase and lowercase English letters.
    * Could you find an algorithm that runs in O(m + n) time?
    ***/
    public static class MinWindowSubstring
    {
        public static void Execute(){
            Console.WriteLine(MinWindowSubstringTest(new string[] { "ADOBECODEBANC", "ABC" }));
            Console.WriteLine(MinWindowSubstringTest(new string[] { "ahffaksfajeeubsne", "jefaa" }));
            Console.WriteLine(MinWindowSubstringTest2("ADOBECODEBANC", "ABC"));
            Console.WriteLine(MinWindowSubstringTest2("ahffaksfajeeubsne", "jefaa"));
        }

        public static string MinWindowSubstringTest(string[] strArr)
        {
            var baseArray = strArr[0];
            var searchItems = strArr[1];

            if (baseArray.Length == searchItems.Length)
                return baseArray;

            var dict = new Dictionary<char, int>();
            foreach (var item in searchItems)
            {
                if (dict.ContainsKey(item))
                    dict[item] += 1;
                else
                    dict.Add(item, 1);
            }

            var left = 0;
            var right = baseArray.Length;
            var count = 0;
            var retValue = "";
            for (var i = 0; i < baseArray.Length; i++)
            {
                if (dict.ContainsKey(baseArray[i]) && --dict[baseArray[i]] >= 0)
                {
                    count++;
                }

                while (count == searchItems.Length)
                {
                    if (right > i - left)
                    {
                        right = i - left;
                        retValue = baseArray.Substring(left, right + 1);
                    }

                    if (dict.ContainsKey(baseArray[left]) && ++dict[baseArray[left]] > 0)
                        count--;

                    left++;
                }
            }
            return retValue;
        }


        public static string MinWindowSubstringTest2(string s, string t)
        {
            var dict = new Dictionary<char, int>();
            for (int i = 0; i < t.Length; i++)
            {
                if (dict.ContainsKey(t[i]))
                {
                    dict[t[i]]++;
                }
                else
                {
                    dict.Add(t[i], 1);
                }
            }

            var res = string.Empty;
            var len = s.Length + 1;
            var start = 0;
            var count = t.Length;
            for (int i = 0; i < s.Length; i++)
            {
                if (dict.ContainsKey(s[i]))
                {
                    if (dict[s[i]]-- > 0)
                    {
                        count--;
                    }
                }

                while (count == 0)
                {
                    if (len > i - start + 1)
                    {
                        len = i - start + 1;
                        res = s.Substring(start, len);
                    }

                    if (dict.ContainsKey(s[start]))
                    {
                        if (dict[s[start]]++ >= 0)
                        {
                            count++;
                        }
                    }
                    start++;
                }
            }
            return res;
        }
    }
}
