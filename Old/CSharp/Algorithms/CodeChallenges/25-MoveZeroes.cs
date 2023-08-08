namespace Algorithms.CodeChallenges
{
    /***
    * Given an array of nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    * Example: input=[0,1,0,3,12] output=[1,3,12,0,0]
    * Don't make a copy of the array.
    ***/
    public static class MoveZeroes
    {
        public static void Execute(){
            Console.WriteLine($"Moving zeroes of [0,1,0,3,12] is: {string.Join(",", moveZeroes(new[]{0,1,0,3,12}))}");
        }

        private static int[] moveZeroes(int[] nums) {
            var index = 0;
            for (var i = 0; i < nums.Length; i++)
            {
                if(nums[i] != 0) {
                    nums[index++] = nums[i];
                }
            }

            for (var i = index; i < nums.Length; i++)
            {
                nums[i] = 0;
            }

            return nums; 
        }
    }
}