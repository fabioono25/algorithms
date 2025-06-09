# Helper function (used by the out-of-place version)
def find_smallest(arr):
  """
  Finds the index of the smallest element in a given list.

  Args:
    arr: The list to search.

  Returns:
    The index of the smallest element in the list.
  """
  smallest_val = arr[0] # stores the smallest value encountered so far
  smallest_idx = 0      # stores the index of the smallest value
  for i in range(1, len(arr)):
    if arr[i] < smallest_val:
      smallest_val = arr[i]
      smallest_idx = i
  return smallest_idx

# Simple Solution: In-Place Selection Sort
def selection_sort_simple_inplace(arr):
  """
  Sorts a list in-place using the Selection Sort algorithm.

  Args:
    arr: The list of items to be sorted. Modifies the list directly.

  Returns:
    None (the list is sorted in-place).
  """
  n = len(arr)
  # Traverse through all array elements
  for i in range(n):
    # Find the minimum element in the remaining unsorted part of the array
    min_idx = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j

    # Swap the found minimum element with the first element of the unsorted part
    # This places the minimum element at its correct sorted position.
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr # Conventionally, in-place sorts might return None, but returning arr is also common.

# Robust Solution: Out-of-Place Selection Sort (Conceptual)
def selection_sort_robust_outofplace(input_arr):
  """
  Sorts a list using an out-of-place Selection Sort approach.
  This version builds a new sorted list by repeatedly finding the smallest
  element in a working copy of the input list and moving it to the new list.

  Args:
    input_arr: The list of items to be sorted. This list is not modified.

  Returns:
    A new list containing the elements of input_arr in sorted order.
  """
  arr_copy = list(input_arr) # Make a copy to avoid modifying the original list
  new_sorted_arr = []

  # Iterate len(arr_copy) times, each time finding the smallest
  # element in the current arr_copy, adding it to new_sorted_arr,
  # and removing it from arr_copy.
  for _ in range(len(input_arr)): # Iterate based on original length
    smallest_idx = find_smallest(arr_copy) # find_smallest operates on the shrinking copy
    new_sorted_arr.append(arr_copy.pop(smallest_idx))

  # Time Complexity:
  # - The outer loop runs N times.
  # - find_smallest takes O(M) where M is the current size of arr_copy. M decreases from N to 1.
  #   So, find_smallest calls sum up to O(N^2).
  # - arr.pop(smallest_idx): In Python, list.pop(i) is O(N-i) in the worst case (if i is small)
  #   or O(k) where k is number of elements to shift. If smallest_idx is often 0, this is O(M).
  #   If pop is O(M) on average in this loop, then N * O(M) contributes to O(N^2).
  #   Overall, it's dominated by O(N^2).
  # Space Complexity:
  # - O(N) for arr_copy.
  # - O(N) for new_sorted_arr.
  # - Total: O(N) auxiliary space.
  return new_sorted_arr

# Jedi Solution: Analysis and Properties of In-Place Selection Sort
# The following analysis refers to `selection_sort_simple_inplace`.

# Time Complexity:
# - Comparisons:
#   The outer loop runs N times.
#   The inner loop (for finding the minimum) runs N-1, N-2, ..., 1 times.
#   Total comparisons = (N-1) + (N-2) + ... + 1 = N*(N-1)/2, which is O(N^2).
#   This is true for best, average, and worst cases as the search for the minimum
#   always scans the rest of the unsorted part.
# - Swaps:
#   There is exactly one swap per iteration of the outer loop (unless the element
#   is already in its correct position, but the swap operation `arr[i], arr[min_idx] = arr[min_idx], arr[i]`
#   still occurs).
#   So, there are N swaps (or N-1 swaps, depending on implementation details). This is O(N) swaps.
#   This is a key advantage of Selection Sort: minimal number of writes to memory.

# Space Complexity:
# - O(1) auxiliary space.
#   The sort is performed in-place. Only a few variables are needed for storing indices
#   (min_idx, i, j) and for the temporary variable during swap (Python handles this tuple swap implicitly).
#   The input array itself is not counted as auxiliary space.

# Stability:
# - The standard implementation of Selection Sort (like `selection_sort_simple_inplace`) is NOT stable.
#   Stability means that if two elements have the same value, their relative order in the
#   sorted output is the same as their relative order in the input.
#   Consider an array like `[ (3, 'a'), (2, 'b'), (3, 'c') ]`.
#   In the first pass, (2, 'b') will be selected and swapped with (3, 'a').
#   Array becomes: `[ (2, 'b'), (3, 'a'), (3, 'c') ]`.
#   Now, when sorting the rest, (3, 'a') might be swapped with (3, 'c') if the comparison
#   for min_idx doesn't prioritize the original order, or if it's chosen as the minimum.
#   More simply, if `arr = [3a, 1, 3b]` (where 3a and 3b are equal in value but distinguishable):
#   1. Smallest is 1. Swap 3a and 1: `[1, 3a, 3b]`. The relative order of 3a and 3b is preserved.
#   If `arr = [3a, 3b, 1]`:
#   1. Smallest is 1. Swap 3a and 1: `[1, 3b, 3a]`. The relative order of 3a and 3b is reversed.
#   The swap operation can change the relative order of equal elements.
# - To make Selection Sort stable, instead of swapping, elements could be shifted.
#   When the minimum element is found, it's inserted into its correct position by
#   shifting all intermediate elements one position to the right. This is more like
#   Insertion Sort and increases complexity/operations.

# Use Cases:
# - When memory writes are costly: Selection Sort makes O(N) swaps, which is the minimum
#   possible for any comparison sort that makes progress by one element per main iteration.
#   This can be beneficial for flash memory or EEPROMs where writes are expensive or limited.
# - When N is small: For small datasets, the O(N^2) complexity is not a major drawback,
#   and its simplicity can be an advantage.
# - Educational purposes: It's a simple algorithm to understand and implement.

# Comparison with other O(N^2) sorts:
# - Bubble Sort:
#   - Also O(N^2) time complexity.
#   - Bubble Sort typically involves many more swaps (O(N^2) in the worst case) than Selection Sort.
#   - Bubble Sort can be "adaptive" if optimized (stops early if no swaps in a pass),
#     whereas Selection Sort always performs the full N-1 passes.
# - Insertion Sort:
#   - O(N^2) average and worst-case time, but O(N) in the best case (nearly sorted data).
#   - Insertion Sort is generally faster than Selection Sort in practice for most inputs
#     due to better cache performance and fewer comparisons if data is partially sorted.
#   - Insertion Sort is stable.
#   - Number of swaps in Insertion Sort can be up to O(N^2).

# Example Usage
print("Original list:", [5, 3, 6, 2, 10, 1])

# Test Simple In-Place Solution
list1 = [5, 3, 6, 2, 10, 1]
selection_sort_simple_inplace(list1)
print("Simple In-Place Sorted:", list1) # => [1, 2, 3, 5, 6, 10]

list2 = [5, 11, 6, 2, 10, 0, -5]
selection_sort_simple_inplace(list2)
print("Simple In-Place Sorted:", list2) # => [-5, 0, 2, 5, 6, 10, 11]

list_empty_simple = []
selection_sort_simple_inplace(list_empty_simple)
print("Simple In-Place Sorted (empty):", list_empty_simple) # => []

list_single_simple = [42]
selection_sort_simple_inplace(list_single_simple)
print("Simple In-Place Sorted (single):", list_single_simple) # => [42]


# Test Robust Out-of-Place Solution
list3 = [5, 3, 6, 2, 10, 1]
sorted_list3 = selection_sort_robust_outofplace(list3)
print("Robust Out-of-Place Sorted:", sorted_list3) # => [1, 2, 3, 5, 6, 10]
print("Original list3 (should be unchanged):", list3) # => [5, 3, 6, 2, 10, 1]

list4 = [5, 11, 6, 2, 10, 0, -5]
sorted_list4 = selection_sort_robust_outofplace(list4)
print("Robust Out-of-Place Sorted:", sorted_list4) # => [-5, 0, 2, 5, 6, 10, 11]

list_empty_robust = []
sorted_empty_robust = selection_sort_robust_outofplace(list_empty_robust)
print("Robust Out-of-Place Sorted (empty):", sorted_empty_robust) # => []

list_single_robust = [42]
sorted_single_robust = selection_sort_robust_outofplace(list_single_robust)
print("Robust Out-of-Place Sorted (single):", sorted_single_robust) # => [42]