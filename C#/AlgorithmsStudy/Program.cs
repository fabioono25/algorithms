using System;
using System.Collections;
using System.IO;

namespace AlgorithmsStudy
{
    class Program
    {
        static void Main(string[] args)
        {
            //IceCreamProblem.Execute();
            BinarySearch.Execute();
        }
    }

    #region Problems

    //Binary Search Implementation - O(log n)
    public class BinarySearch {

        public static void Execute(){
            var arr = new int[] {1, 2, 5, 6, 7, 8, 9, 11, 99, 123};

            var itemFound = binarySearchIteractive(arr, 99);
            Console.WriteLine(itemFound);

            itemFound = binarySearchRecursive(arr, 99);
            Console.WriteLine(itemFound);
        }

        public static bool binarySearchIteractive(int[] array, int x) {
            var left = 0;
            var right = array.Length-1;

            while (left <= right)
            {
                var mid = left + ((right - left) / 2);

                if (array[mid] == x){
                    return true;
                } else if (x < array[mid]) {
                    right = mid + 1;
                } else {
                    left = mid + 1;
                }
            }
            return false;
        }

        public static bool binarySearchRecursive(int[] array, int x) {
            return binarySearchRecursive(array, x, 0, array.Length-1) ;
        }

        public static bool binarySearchRecursive(int[] array, int x, int left, int right) {

            if (left > right)
                return false;

            var mid = (left + right) / 2;

            if (array[mid] == x) {
                return true;
            } else if (x < array[mid]) {
                return binarySearchRecursive(array, x, left, mid - 1);
            } else {
                return binarySearchRecursive(array, x, mid + 1, right);
            }
        }
    }


    //Problem: Ice Cream Parlor (iceCream.jpeg)
    //Find the indices of two items on the menu that allow us to spend all our money
    //The idea is to use Binary Search to solve the problem
    //https://www.hackerrank.com/challenges/icecream-parlor/problem
    public class IceCreamProblem {
        public static void Execute(){
            var result = findChoices(new int[]{3, 9, 7, 1, 11, 6, 5}, 10);
        }

        //return by order of appearance in array
        public static int[] findChoices(int[] menu, int money) {
            
            var sortedMenu = (int[])menu.Clone();
            Array.Sort(sortedMenu);

            for (int i = 0; i < sortedMenu.Length; i++) //{1, 3, 5, 6, 7, 9, 11}
            {
                int complement = money - sortedMenu[i];
                int location = Array.BinarySearch(sortedMenu, i+1, sortedMenu.Length-1, complement); //if the item is not contained, it'll return negative

                if (location >= 0 && location < sortedMenu.Length && sortedMenu[location] == complement) {
                    int[] indexes = getIndexesFromValues(sortedMenu, sortedMenu[i], complement);
                    return indexes;
                }
            }

            return null;
        }

        private static int[] getIndexesFromValues(int[] menu, int value1, int value2)
        {
            int index1 = indexOf(menu, value1, -1);
            int index2 = indexOf(menu, value2, index1);

            int[] indexes = { Math.Min(index1, index2), Math.Max(index1, index2) };

            return indexes;
        }

        private static int indexOf(int[] menu, int value, int excludeThis)
        {
            for (int i = 0; i < menu.Length; i++)
            {
                if (menu[i] == value && i != excludeThis)
                    return i;
            }

            return -1;
        }
    }

    public abstract class AbstractX {

        public AbstractX()
        {
            
        }

        public int MyProperty { get; set; }

        public void returnValue() 
        { 
            Console.WriteLine("asdas");
        }

        public abstract void rest();

    }

    public interface ITest {
        string Name { get; set; }

        void test();
    }

    public class InheritedClass : AbstractX, ITest
    {
        
        public string Name { get => throw new NotImplementedException(); set => throw new NotImplementedException(); }

        public override void rest()
        {

            throw new NotImplementedException();
        }

        public void test()
        {
            throw new NotImplementedException();
        }
    }

    public struct TestStruct {
    }

    #endregion
}
