using System;
namespace Algorithms.CodeChallenges
{
    /***
    * Given an array of integers, return indices of the two numbers such they add up to a specific target.
    * given [2, 7, 11, 15], target = 9, as num[0] + num[1] = 9, return [0, 1]
    ***/
    public static class TwoSum
    {
        public static void Execute(){
            Console.WriteLine($"{String.Join(",", twoSum(new int[]{2, 7, 11, 15}, 9))}");
            Console.WriteLine($"{String.Join(",", twoSumWithDictionary(new int[]{2, 7, 11, 15}, 9))}");
        }

        private static int[] twoSum(int[] n, int target) {
            for (var i = 0; i < n.Length; i++){
                var x = n[i];
                for (var j = i+1; j < n.Length; j++){
                    if (x + n[j] == target)
                        return new int[]{ i, j };
                }
            }
            return new int[]{-1,-1};
        }

        private static int[] twoSumWithDictionary(int[] n, int target) {
            var dict = new Dictionary<int, int>();

            for (var i = 0; i < n.Length; i++){
                var difference = target - n[i];

                if (dict.ContainsKey(difference)) {
                    return new int[] { i, dict[difference] };
                }

                dict.Add(n[i], i);
            }
            return new int[] { -1, -1 };;
        }
    }
}