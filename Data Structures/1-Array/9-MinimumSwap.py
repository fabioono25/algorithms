# Given an unordered array consisting of consecutive integers [1, 2, 3, ..., n] without any duplicates, find the minimum number of swaps required to sort the array in ascending order.

# Example
# arr = [7, 1, 3, 2, 4, 5, 6]
# Perform the following steps:
# swap 1 and 7
# swap 2 and 7
# swap 3 and 7
# swap 4 and 7
# swap 5 and 7
# swap 6 and 7
# Now, the array is sorted.

# Time Complexity: O(N) - Space Complexity: O(1)
def minimum_swaps(arr):
  swaps = 0
  for i in range(len(arr)):
    while arr[i] != i + 1:
      arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
      swaps += 1
  return swaps

print(minimum_swaps([7, 1, 3, 2, 4, 5, 6]))