namespace Algorithms.CodeChallenges
{
    /***
    * Row of n houses, each can be painted in red, blue or green. the cost for each house is different. 
    * Paint all the houses such that no two adjacent houses have the same color.
    * cost is represented by n x 3 cost matrix. Ex: costs[0][0] is the cost of painting house 0 with color red.
    * costs[1][2] is the cost of painting house 1 with color green and so. Find the minimum cost to paint all houses.
    * input[[17,2,17],[16,16,5],[14,3,19]], output: 10
    * (paint house 0 in blue (2, just randomly chosen), house 1 in green (5), house 2 in blue (3) - mincost: 2+5+3=10)
    ***/
    public static class PaintHouse
    {
        public static void Execute(){

            var input = new int[][]
            {
                new[] { 17, 2, 17 },
                new[] { 16,16,5 },
                new[] { 14, 3, 19 }
            };

            Console.WriteLine($"minCost: {minCost(input)}");
        }

        private static int minCost(int[][] costs) {
            if (costs == null || costs.Length == 0)
                return 0;

            for (int i = 1; i < costs.Length; i++)
            {
                costs[i][0] += Math.Min(costs[i-1][1], costs[i-1][2]);
                costs[i][1] += Math.Min(costs[i-1][0], costs[i-1][2]);
                costs[i][2] += Math.Min(costs[i-1][0], costs[i-1][1]);
            }

            return Math.Min(Math.Min(costs[costs.Length-1][0], costs[costs.Length-1][1]), costs[costs.Length-1][2]);
        }
    }
}