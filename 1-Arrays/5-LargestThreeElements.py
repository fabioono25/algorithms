# import array
# arr = array.array('i', [1, 2, 3, 4, 5])

# Given an array with all distinct elements, find the largest three elements. Expected time complexity is O(n) and extra space is O(1).
# Input: arr[] = {10, 4, 3, 50, 23, 90} Output: 90, 50, 23

# Simple solution. Time Complexity: O(n) Space Complexity: O(1)
def peakElement(arr):
    if len(arr) < 3:
        return None

    if len(arr) == 3:
        return arr

    ret = [0, 0, 0]

    for i in range(len(arr)):
        if (arr[i] > ret[0]):
            ret[2], ret[1], ret[0] = ret[1], ret[0], arr[i]
        elif (arr[i] > ret[1]):
            ret[2], ret[1] = ret[1], arr[i]
        elif (arr[i] > ret[2]):
            ret[2] = arr[i]

    return ret

# another option would be solving using a sorting algorithm, and then return the last 3 elements of the array. 
# Time Complexity: O(n log n) Space Complexity: O(1)
def peakElement2(arr):
    if len(arr) < 3:
        return None

    arr.sort()

    return arr[-3:]


print(peakElement([10, 4, 3, 50, 23, 90]))