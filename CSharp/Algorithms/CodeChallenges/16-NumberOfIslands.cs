namespace Algorithms.CodeChallenges
{
    /***
    * Given a 2d grid map of '1' land and '0' water, count the number of islands
    * An island is surrounded by water and it's formed by connecting adjacent lands horizontally and vertically.
    * Assume that all four edges of the grid are all surrounded by water
    * 11110 
    * 11010
    * 11000
    * 00000
    * Output: 1
    * 11000 
    * 11000
    * 00100
    * 00011
    * Output: 3   
    ***/
    public static class NumberOfIslands
    {
        public static void Execute(){
            // jagged array
           //var grid = new int[][] {
           // new int[] {1, 1, 0, 0, 0},
           // new int[] {1, 1, 0, 0, 0},
           // new int[] {0, 0, 1, 0, 0},
           // new int[] {0, 0, 0, 1, 1}
           //};
           var grid = new int[][] {
                new int[] {1, 0, 1, 0, 1},
                new int[] {1, 1, 0, 0, 0},
                new int[] {0, 0, 1, 0, 0},
                new int[] {0, 0, 0, 1, 1}
           };
           Console.WriteLine($"Number of islands: {numberOfIslands(grid)}");
        }

        private static int numberOfIslands(int[][] grid) {

            if (grid == null || grid.Length == 0)
                return 0;

            var numberOfIslands = 0;
            for (var i = 0; i < grid.Length; i++)
            {
                for (int j = 0; j < grid[i].Length; j++)
                {
                    if (grid[i][j] == 1)
                    {
                        numberOfIslands += EvaluateIslandsDfs(grid, i, j);
                    }
                }
            }    

            return numberOfIslands;
        }

        private static int EvaluateIslandsDfs(int[][] grid, int i, int j)
        {
            if (i < 0 || i >= grid.Length || j < 0 || j >= grid[i].Length || grid[i][j] == 0)
                return 0;

            grid[i][j] = 0;
            EvaluateIslandsDfs(grid, i + 1, j);
            EvaluateIslandsDfs(grid, i - 1, j);
            EvaluateIslandsDfs(grid, i, j + 1);
            EvaluateIslandsDfs(grid, i, j - 1);

            return 1;
        }
    }
}