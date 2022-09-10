namespace Algorithms.CodeChallenges
{
    /***
    * Return the index of the peak element (the element that is greater than its neighbors)
    * [1, 2, 3, 1] = 2, because 3 is a peak element
    * [1,2,1,3,5,6,4] = 1 or 5, because 2 and 6 are peak elements
    ***/
    public static class PeakElement
    {
        public static void Execute(){
            Console.WriteLine($"Peak element of array [1, 2, 3, 1] is: {peakElement(new int[]{1, 2, 3, 1})}");
            Console.WriteLine($"Peak element of array [1,2,1,3,5,6,4] is: {peakElement(new int[]{1,2,1,3,5,6,4})}");

            Console.WriteLine($"Peak element of array with BS [1, 2, 3, 1] is: {peakElementWithBinarySearch(new int[]{1, 2, 3, 1})}");
            Console.WriteLine($"Peak element of array with BS [1,2,1,3,5,6,4] is: {peakElementWithBinarySearch(new int[]{1,2,1,3,5,6,4})}");            
        }

        private static int peakElement(int[] n) {
            for (var i = 1; i < n.Length-1; i++)
                if (n[i] > n[i-1] && n[i] > n[i+1])
                    return i;

            return -1;
        }

        private static int peakElementWithBinarySearch(int[] n) {
            var left = 0;
            var right = n.Length - 1;

            while (left < right)
            {
                var mid = left + (right - left) / 2;

                if (n[mid] < n[mid + 1])
                    left += 1;
                else
                    right = mid;
            }

            return left;
        }
    }
}