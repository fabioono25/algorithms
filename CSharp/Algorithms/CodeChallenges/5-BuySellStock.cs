namespace Algorithms.CodeChallenges
{
    /***
    * you have an array representing the indexes as days (index 0 = day 1) and respective prices
    * the objective is buy with the lowest price and sell after with the highest price (best transaction)
    * [7, 1, 5, 3, 6, 4] => buy on day 2 (1) and sell on day 5 (6) with a profit (output 5).
    * [7, 6, 4, 3, 1] => it's not possible to obtain profit (output 0)
    ***/
    public static class BuySellStock
    {
        public static void Execute(){

           Console.WriteLine($"Max profit for [7, 1, 5, 3, 6, 4] is: {maxProfit(new[] {7, 1, 5, 3, 6, 4})}");
           Console.WriteLine($"Max profit for [7, 6, 4, 3, 1] is: {maxProfit(new[] {7, 6, 4, 3, 1})}");
        }

        // assuming that there are at least two days (array.length > 1)
        private static int maxProfit(int[] prices) {
            var minPrice = prices[0];
            var maxPrice = 0;

            for (var i=1; i < prices.Length; i++) {
                if (prices[i] < minPrice) {
                    minPrice = prices[i];
                }else {
                    maxPrice = Math.Max(maxPrice, prices[i] - minPrice);
                }
            }

            return maxPrice;
        }
    }
}