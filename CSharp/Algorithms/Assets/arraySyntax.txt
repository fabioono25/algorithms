namespace Algorithms.DataStructures.Arrays
{
    public class Tests
    {
        // array definition
        int[] array1 = new int[5];
        int[,] multi = new int[2,4];
        int[][] jagged = new int[6][];

        public static void Execute() {
            var arr = new [] {1, '2', 3, 10, 20, 305, 123, 232};
            Console.WriteLine(string.Join(",", arr));

            // adding at the end of the array
            arr = arr.Append(1001).ToArray();

            // adding in the beginning of the array
            arr = arr.Prepend(0).ToArray();

            // adding in the middle of the array
            // arr.Insert - not supported, you should use an external array in order to accomplish it

            // remove from array - not an easy task as well, but you can use Linq to work around on that
            var x = arr.ToList();
            x.RemoveAt(2);

            var index = Array.IndexOf(arr, 20);
            arr = arr.Where((val, idx) => idx != index).ToArray();

            // changing value of an existing array
            arr[2] = 999;
        }
    }
}