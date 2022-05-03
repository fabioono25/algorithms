namespace Algorithms.Arrays
{

// the objective is to reverse an one-dimensional array of integers in linear time complexity O(n)
// no additional memory should be used
// example: input [1,2,3,4,5] then output is [5,4,3,2,1]
  public static class ReverseArray {
    public static void Execute() {
      Console.WriteLine(string.Join(", ", reverse(new [] {1,2,3,4,5})));
    }

    public static int[] reverse(int[] numbers) {
      var startIndex = 0;
      var lastIndex = numbers.Length-1;

      while (startIndex < lastIndex)
      {
        (numbers[startIndex], numbers[lastIndex]) = (numbers[lastIndex], numbers[startIndex]);
        startIndex+=1;
        lastIndex-=1;
      }

      return numbers;
    }
  }
}