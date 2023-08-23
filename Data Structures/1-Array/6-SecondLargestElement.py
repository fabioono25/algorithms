# import array
# arr = array.array('i', [1, 2, 3, 4, 5])

# Given an array of integers, our task is to write a program that efficiently finds the second-largest element present in the array. 
# Input: arr[] = {12, 35, 1, 10, 34, 1} Output: The second largest element is 34.

# Simple solution. Time Complexity: O(n) Space Complexity: O(1)
def secondLargestElement(arr):
    first, second = 0, 0

    for i in range(len(arr)):
        if (arr[i] > first):
            second, first = first, arr[i]
        elif (arr[i] > second):
            second = arr[i]

    return second

# another option would be solving using a sorting algorithm, and then return the last 3 elements of the array. 
# Time Complexity: O(n log n) Space Complexity: O(1)
def secondLargestElement2(arr):
    arr.sort()

    return arr[-2]


print(secondLargestElement([12, 35, 1, 10, 34, 1]))
print(secondLargestElement2([12, 35, 1, 10, 34, 1]))