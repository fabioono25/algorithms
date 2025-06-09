# Simple Solution (Out-of-Place)
def quicksort_simple_outofplace(array):
  """
  Sorts an array using a simple, non-in-place Quicksort algorithm.
  This version is easy to understand but uses O(N) auxiliary space
  due to the list comprehensions creating new lists for 'less' and 'greater'
  elements in each recursive call.

  Args:
    array: The list of items to sort.

  Returns:
    A new list containing the sorted items.
  """
  if len(array) < 2:
    # Base case: arrays with 0 or 1 element are already sorted.
    return array
  
  pivot = array[0] # Choose the first element as the pivot.
  # Partitioning: elements less than or equal to pivot, and elements greater than pivot.
  # These comprehensions create new lists, hence not in-place.
  less = [i for i in array[1:] if i <= pivot]
  greater = [i for i in array[1:] if i > pivot]

  # Recursively sort the sub-arrays and combine.
  return quicksort_simple_outofplace(less) + [pivot] + quicksort_simple_outofplace(greater)

# Robust Solution (In-Place with Lomuto Partition)
def partition_lomuto(arr, low, high):
    """
    Partitions the array using Lomuto's partitioning scheme.
    The pivot is chosen as the last element (arr[high]).
    Elements smaller than or equal to the pivot are moved to its left,
    and larger elements to its right.

    Args:
        arr: The list to be partitioned.
        low: Starting index of the segment to partition.
        high: Ending index of the segment to partition.

    Returns:
        The index where the pivot is placed.
    """
    pivot = arr[high]  # Choose the last element as pivot
    i = low - 1        # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1  # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in correct position
    return i + 1  # Return pivot index

def quicksort_robust_inplace_lomuto(arr, low, high):
    """
    Sorts an array in-place using Quicksort with Lomuto partitioning.

    Args:
        arr: The list to be sorted.
        low: Starting index for sorting.
        high: Ending index for sorting.
    """
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition_lomuto(arr, low, high)

        # Separately sort elements before partition and after partition
        quicksort_robust_inplace_lomuto(arr, low, pi - 1)
        quicksort_robust_inplace_lomuto(arr, pi + 1, high)

def sort_with_lomuto(arr):
    """
    Wrapper function to sort an array using Quicksort with Lomuto partition.
    Modifies the array in-place.
    """
    if not arr: # Handle empty list case
        return arr
    quicksort_robust_inplace_lomuto(arr, 0, len(arr) - 1)
    return arr

# Jedi Solution (In-Place with Hoare Partition and Analysis)
def partition_hoare(arr, low, high):
    """
    Partitions the array using Hoare's original partitioning scheme.
    The pivot is chosen as the first element (arr[low]).
    It returns an index `j` such that all arr[low...j] are less than or
    equal to pivot and all arr[j+1...high] are greater than or equal to pivot.
    The pivot itself may not be at index `j`.

    Args:
        arr: The list to be partitioned.
        low: Starting index of the segment.
        high: Ending index of the segment.

    Returns:
        The index where the array is partitioned.
    """
    pivot = arr[low]  # Choose the first element as pivot
    i = low - 1       # Pointer from the left
    j = high + 1      # Pointer from the right

    while True:
        # Find element on left that should be on right
        i += 1
        while arr[i] < pivot:
            i += 1

        # Find element on right that should be on left
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If pointers met or crossed, partition is done
        if i >= j:
            return j  # j is the partition point

        # Swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]

def quicksort_jedi_inplace_hoare(arr, low, high):
    """
    Sorts an array in-place using Quicksort with Hoare partitioning.

    Args:
        arr: The list to be sorted.
        low: Starting index for sorting.
        high: Ending index for sorting.
    """
    if low < high:
        # pi is partitioning index. Note that with Hoare's scheme,
        # the pivot is not necessarily in its final sorted position after partitioning.
        # The partition index pi divides the array into two parts:
        # arr[low...pi] and arr[pi+1...high]
        pi = partition_hoare(arr, low, high)

        # Recursively sort the two parts.
        # For Hoare, the element at pi might not be the pivot or in its final place,
        # so the recursive calls include pi in the first part.
        quicksort_jedi_inplace_hoare(arr, low, pi)
        quicksort_jedi_inplace_hoare(arr, pi + 1, high)

def sort_with_hoare(arr):
    """
    Wrapper function to sort an array using Quicksort with Hoare partition.
    Modifies the array in-place.
    """
    if not arr: # Handle empty list
        return arr
    quicksort_jedi_inplace_hoare(arr, 0, len(arr) - 1)
    return arr

# Analysis for Jedi Solution (In-Place Quicksort):
# - Pivot Selection:
#   - The choice of pivot significantly impacts Quicksort's performance.
#   - Worst Case: Consistently picking the smallest or largest element (e.g., in a sorted/reverse-sorted array with arr[0] or arr[high] as pivot). This leads to O(N^2) complexity.
#   - Good Strategies:
#     - Median-of-Three: Choose the pivot as the median of the first, middle, and last elements of the array segment. This reduces the chance of worst-case pivot selection.
#     - Randomized Pivot: Pick a random element as the pivot. Statistically, this makes worst-case scenarios very unlikely.
# - Time Complexity:
#   - Average Case: O(N log N). This occurs when partitions are reasonably balanced. Each partitioning step takes O(N) time, and there are O(log N) recursive levels.
#   - Worst Case: O(N^2). Occurs with poor pivot choices leading to highly unbalanced partitions (e.g., one sub-array of size N-1 and the other of size 0).
# - Space Complexity:
#   - In-Place Versions (Lomuto, Hoare):
#     - Average Case: O(log N) auxiliary space for the recursion call stack.
#     - Worst Case: O(N) auxiliary space for the recursion stack if partitions are extremely unbalanced (leading to a deep recursion tree).
#   - Simple Out-of-Place Version (`quicksort_simple_outofplace`):
#     - O(N) auxiliary space due to the list comprehensions creating new lists for `less` and `greater` parts in each call. In the worst-case recursion depth, this could lead to O(N^2) space if not careful, but typically it's managed by Python's garbage collection, and the main concern is O(N) for the copies at each level of O(log N) or O(N) depth. The primary space cost is from the largest set of sub-problem arrays existing simultaneously.
# - Stability:
#   - Quicksort (both Lomuto and Hoare partition based implementations) is NOT a stable sort.
#   - The relative order of equal elements can change because elements are swapped across large distances based on their relation to the pivot, without regard to their original order if they are equal to another element.
# - Optimizations for In-Place Quicksort:
#   - Tail Call Optimization (Conceptual in Python): In languages that support it, tail recursion for the larger partition's sort can be optimized to reduce stack depth. Python doesn't directly optimize tail calls.
#   - Hybrid Approach (e.g., Introsort): Switch to a non-recursive sorting algorithm like Insertion Sort for small subarrays (e.g., when size < 10-20). Insertion Sort is efficient for small N and avoids the overhead of further recursion. Some implementations also switch to Heapsort if recursion depth exceeds a threshold to guarantee O(N log N) worst-case time.


# --- Example Usage ---
def run_tests(sort_function_name, sort_func, is_inplace=False):
    print(f"\n--- Testing: {sort_function_name} ---")

    test_cases = {
        "Regular": [5, 1, 4, 2, 8, 3, 7, 6],
        "Duplicates": [5, 1, 4, 2, 8, 4, 2, 6],
        "Already Sorted": [1, 2, 3, 4, 5, 6, 7, 8],
        "Reverse Sorted": [8, 7, 6, 5, 4, 3, 2, 1],
        "Empty": [],
        "Single Element": [42],
        "Negative Numbers": [-5, 1, -4, 0, 8, -2, 7, 6],
        "Mixed Duplicates": [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    }

    for name, arr_orig in test_cases.items():
        arr_to_sort = list(arr_orig) # Create a copy for sorting, this is passed to the sort function

        expected_sorted_arr = sorted(list(arr_orig)) # For comparison

        if is_inplace:
            # The function should modify arr_to_sort in place.
            # It might return the array or None, we'll use arr_to_sort as the result.
            returned_value = sort_func(arr_to_sort)
            result = arr_to_sort

            # Check if original arr_orig is untouched
            original_untouched = (arr_orig == (test_cases[name])) # Compare arr_orig to its initial state from test_cases

            print(f"Test: {name:18} | Original: {str(test_cases[name]):35} | Sorted: {str(result):35} | Expected: {str(expected_sorted_arr):35} | Original Untouched: {original_untouched}")
            if not original_untouched:
                 print(f"ERROR: In-place function {sort_function_name} MODIFIED the original list for test '{name}'!")
            if returned_value is not None and id(returned_value) != id(result):
                 print(f"INFO: In-place function {sort_function_name} returned a new list object for test '{name}'. Standard in-place functions modify the list and often return None or the list itself.")

        else: # Out-of-place
            # The function should return a new sorted list and not modify arr_to_sort (which is a copy of arr_orig)
            result = sort_func(arr_to_sort)
            original_copy_untouched = (arr_to_sort == arr_orig)

            print(f"Test: {name:18} | Original: {str(arr_orig):35} | Sorted: {str(result):35} | Expected: {str(expected_sorted_arr):35} | Copy Unchanged: {original_copy_untouched}")
            if not original_copy_untouched:
                print(f"ERROR: Out-of-place function {sort_function_name} MODIFIED its input copy for test '{name}'!")

        if result != expected_sorted_arr:
            print(f"FAIL: Result {result} does not match expected {expected_sorted_arr} for test '{name}' with {sort_function_name}")

# Test Simple Solution (Out-of-Place)
run_tests("quicksort_simple_outofplace", quicksort_simple_outofplace, is_inplace=False)

# Test Robust Solution (In-Place with Lomuto Partition)
run_tests("sort_with_lomuto", sort_with_lomuto, is_inplace=True)

# Test Jedi Solution (In-Place with Hoare Partition)
run_tests("sort_with_hoare", sort_with_hoare, is_inplace=True)
