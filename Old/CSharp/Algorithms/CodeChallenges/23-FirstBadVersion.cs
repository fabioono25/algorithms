namespace Algorithms.CodeChallenges
{
    /***
    * we have n versions [1,2,3,4,...,n] and you want to find out the first bad one, which causes all the following ones to be bad.
    * the API bools isBadVersion(version) will return whether the version is bad. Implement a function that find the firs bad version.
    * You should optimize the calls to the API.
    * given n=5, version=4, is the first bad version
    * call isBadVersion(3)=false, isBadVersion(5)=true, isBadVersion(4)=true, then 4 is the first bad version
    ***/
    public static class FirstBadVersion
    {
        public static void Execute(){
            Console.WriteLine($"first bad version: {firstBadVersion(22)}");     
        }

        // O(log N)
        private static int firstBadVersion(int n) {
            // 0 0 0 0 1 1 1 1 - representing bad and good results (Binary Search)
            var left = 1;
            var right = n;

            while (left < right)
            {
                var mid = left + (right - left) / 2;

                if (!isBadVersion(mid))
                {
                    left = mid + 1;
                } else
                {
                    right = mid;
                }
            }

            return left;
        }

        private static bool isBadVersion(int n)
        {
            return n > 5;
        }
    }
}