namespace Algorithms.CodeChallenges
{
    /***
    * given a number, for multiples of 3 = Fizz, multiples of 5 = Buzz, multiple of both = FizzBuzz
    * for others, maintain same
    * return an array with all these values
    ***/
    public static class FizzBuzz
    {
        public static void Execute(){
            Console.WriteLine($"Given 15: {string.Join(",", fizzBuzz(15))}");
            //Console.WriteLine($"[1,2,3,4] contains duplicates: {containsDuplicates(new[] {1,2,3,4})}");            
        }

        private static List<string> fizzBuzz(int n) {

            var result = new List<string>();

            for (int number = 1; number <= n; number++)
            {
                if (number % 3 == 0 && number % 5 == 0)
                    result.Add("FizzBuzz");
                else if (number % 3 == 0)
                    result.Add("Fizz");
                else if (number % 5 == 0)
                    result.Add("Buzz");
                else
                    result.Add(number.ToString());
            }

            return result;
        }
    }
}