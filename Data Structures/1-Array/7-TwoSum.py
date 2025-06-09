# Data Structures/1-Array/7-TwoSum.py
# Problem: Given an array of integers nums and an integer target, return indices
#          of the two numbers such that they add up to target.
# Assumptions (standard version):
#   - Each input would have exactly one solution.
#   - You may not use the same element twice.
#   - You can return the answer in any order.

from typing import List

# --- Simple Solution: Brute Force ---
def two_sum_simple_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Finds two numbers that sum to target using a brute-force approach.
    Time Complexity: O(N^2) - nested loops.
    Space Complexity: O(1) - constant extra space.
    Args:
        nums: List of integers.
        target: The target sum.
    Returns:
        List containing indices of the two numbers, or an empty list if no solution.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n): # Start j from i+1 to avoid using same element twice
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# --- Robust Solution: Hash Table (Dictionary) ---
def two_sum_robust_hashtable(nums: List[int], target: int) -> List[int]:
    """
    Finds two numbers that sum to target using a hash table to store complements.
    Time Complexity: O(N) - one pass through the array.
    Space Complexity: O(N) - in the worst case, all elements are stored in the hash table.
    Args:
        nums: List of integers.
        target: The target sum.
    Returns:
        List containing indices of the two numbers, or an empty list if no solution.
    """
    hash_table = {}  # Stores {number: index}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in hash_table:
            return [hash_table[complement], index]
        hash_table[num] = index
    return []

# --- Jedi Solution: Sorted Array Two-Pointer Approach and Problem Variations ---

def two_sum_jedi_sorted_array(sorted_nums: List[int], target: int) -> List[int]:
    """
    Finds two numbers that sum to target in a SORTED array using the two-pointer technique.
    This version assumes the input array `sorted_nums` is already sorted.
    It returns the 0-based indices of the numbers from the sorted_nums list.
    If original indices from an unsorted array were needed, this approach would require
    storing original indices before sorting or using a different method.

    Time Complexity: O(N) - one pass, as the array is assumed to be sorted.
                     If sorting were part of this function for an unsorted input,
                     it would be O(N log N) dominated by the sort.
    Space Complexity: O(1) - constant extra space.
    Args:
        sorted_nums: List of integers, must be sorted in non-decreasing order.
        target: The target sum.
    Returns:
        List containing 0-based indices of the two numbers from the sorted list,
        or an empty list if no solution.
    """
    left, right = 0, len(sorted_nums) - 1
    while left < right:
        current_sum = sorted_nums[left] + sorted_nums[right]
        if current_sum == target:
            # Note: If original indices were needed, this would be more complex.
            # We'd need to map these sorted_nums indices back to original indices.
            # For this example, we return indices from the sorted_nums.
            return [left, right]
        elif current_sum < target:
            left += 1
        else: # current_sum > target
            right -= 1
    return []

# **Discussion of Jedi Solution & Problem Variations:**

# 1. Time vs. Space Trade-off:
#    - Brute Force: O(N^2) time, O(1) space. Simple but inefficient for large N.
#    - Hash Table: O(N) time, O(N) space. Faster, but uses more memory. This is often
#      the preferred solution for the standard version of the problem if modifications
#      to the array are not allowed or original indices are paramount.
#    - Sorted Array Two-Pointer: O(N log N) time if sorting is needed initially for an unsorted array,
#      then O(N) for the pointer scan. If the array is already sorted, it's O(N) time.
#      Space complexity is O(1) for the pointers if sorting happens in-place (like `list.sort()`).
#      If a copy is made for sorting (like `sorted()`), then it's O(N) space for the copy.
#      This method is very efficient if the array is already sorted or can be sorted.

# 2. Variation: Array is already sorted.
#    - The `two_sum_jedi_sorted_array` function demonstrates this. It's highly efficient.
#    - If original indices are required from an initially unsorted array that you then sort:
#      You could create a list of (value, original_index) tuples, sort this list based on values,
#      then apply the two-pointer method. The result would use the stored original indices.
#      Example: `indexed_nums = sorted([(num, i) for i, num in enumerate(nums)])`
#               Then apply two-pointers to `indexed_nums[k][0]` and return `indexed_nums[k][1]`.

# 3. Variation: Return numbers instead of indices.
#    - All methods can be easily adapted.
#      - Brute Force: `return [nums[i], nums[j]]`
#      - Hash Table: `return [complement, num]`
#      - Sorted Array: `return [sorted_nums[left], sorted_nums[right]]`

# 4. Variation: Multiple pairs sum to target.
#    - The provided solutions return after finding the first pair (as per standard problem statement).
#    - To find all pairs:
#        - Brute Force: Append valid `[i, j]` to a list of results instead of returning.
#        - Hash Table: When `complement in hash_table`, add `[hash_table[complement], index]`
#          to a results list. Don't add `num` to `hash_table` until after checking to handle cases
#          where `num == complement` (e.g., `nums=[3,3]`, `target=6`). Or, if `num` is added first,
#          ensure `hash_table[complement]` is not `index`.
#        - Sorted Array: When `current_sum == target`, add `[left, right]` to results.
#          Then, to find other pairs, increment `left` and decrement `right`.
#          To avoid duplicate pairs with the same numbers, you'd also need to skip over
#          elements equal to `sorted_nums[left]` and `sorted_nums[right]` before continuing.
#          E.g., `while left < right and sorted_nums[left] == sorted_nums[left-1]: left += 1`.

# 5. Variation: Numbers can be very large.
#    - Python handles arbitrarily large integers automatically, so overflow is not an issue
#      for the numbers themselves or their sum during `nums[i] + nums[j]`, `target - num`,
#      or `sorted_nums[left] + sorted_nums[right]`.
#    - In languages with fixed-size integers (like C++ or Java), one would need to be
#      mindful of potential overflows.

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Two Sum Problem ---")
    nums_example = [2, 7, 11, 15]
    target_example = 9
    print(f"\nInput Nums: {nums_example}, Target: {target_example}")
    print(f"Simple (Brute Force): {two_sum_simple_brute_force(list(nums_example), target_example)}")
    print(f"Robust (Hash Table): {two_sum_robust_hashtable(list(nums_example), target_example)}")

    # For Jedi (Sorted Array)
    # If input is unsorted and original indices are not strictly needed for this specific function call's output:
    nums_for_jedi_sort = [15, 7, 2, 11] # Unsorted version of nums_example
    target_for_jedi_sort = 9
    # Create a sorted version for the function
    # Note: two_sum_jedi_sorted_array returns indices *from the sorted array*
    sorted_version = sorted(list(nums_for_jedi_sort))
    print(f"\nInput Nums for Jedi (unsorted then sorted): {nums_for_jedi_sort} -> {sorted_version}, Target: {target_for_jedi_sort}")
    print(f"Jedi (Sorted Array Two-Pointer on {sorted_version}): {two_sum_jedi_sorted_array(sorted_version, target_for_jedi_sort)}")
    # The output [0, 1] refers to indices in `sorted_version` ([2,7,11,15]), so elements 2 and 7.

    # Example with a different list for sorted array method
    nums_sorted_example_2 = [1, 3, 4, 5, 7, 10, 11] # Already sorted
    target_sorted_example_2 = 12 # 5 + 7 = 12 (indices 3, 4) or 1 + 11 = 12 (indices 0, 6)
                                 # The two-pointer should find one such pair.
    print(f"\nInput Nums for Jedi (already sorted): {nums_sorted_example_2}, Target: {target_sorted_example_2}")
    print(f"Jedi (Sorted Array Two-Pointer): {two_sum_jedi_sorted_array(nums_sorted_example_2, target_sorted_example_2)}")


    print("\n--- Testing with no solution ---")
    nums_no_solution = [1, 2, 3, 5]
    target_no_solution = 10
    print(f"Input Nums: {nums_no_solution}, Target: {target_no_solution}")
    print(f"Simple (Brute Force) No Solution: {two_sum_simple_brute_force(nums_no_solution, target_no_solution)}")
    print(f"Robust (Hash Table) No Solution: {two_sum_robust_hashtable(nums_no_solution, target_no_solution)}")
    # For sorted array, sort it first
    print(f"Jedi (Sorted Array) No Solution (on {sorted(nums_no_solution)}): {two_sum_jedi_sorted_array(sorted(nums_no_solution), target_no_solution)}")

    print("\n--- Testing with negative numbers ---")
    nums_negative = [-1, -3, 5, 7, 2]
    target_negative = 4 # -1 + 5 = 4
    print(f"Input Nums: {nums_negative}, Target: {target_negative}")
    print(f"Simple (Brute Force): {two_sum_simple_brute_force(list(nums_negative), target_negative)}")
    print(f"Robust (Hash Table): {two_sum_robust_hashtable(list(nums_negative), target_negative)}")
    sorted_negative = sorted(list(nums_negative))
    print(f"Jedi (Sorted Array on {sorted_negative}): {two_sum_jedi_sorted_array(sorted_negative, target_negative)}")

    print("\n--- Testing with zero in numbers ---")
    nums_zero = [0, 4, 3, 0]
    target_zero_sum = 0 # 0 + 0 = 0
    print(f"Input Nums: {nums_zero}, Target: {target_zero_sum}")
    print(f"Simple (Brute Force): {two_sum_simple_brute_force(list(nums_zero), target_zero_sum)}")
    print(f"Robust (Hash Table): {two_sum_robust_hashtable(list(nums_zero), target_zero_sum)}")
    sorted_zero = sorted(list(nums_zero))
    print(f"Jedi (Sorted Array on {sorted_zero}): {two_sum_jedi_sorted_array(sorted_zero, target_zero_sum)}")

    # Example for Jedi discussion: needing original indices from sorted array requires more complex setup.
    # If we had nums = [3, 2, 4] and target = 6:
    # Brute force: [1, 2] (for 2, 4)
    # Hash table: [1, 2] (for 2, 4)
    # Jedi (if we sorted it to [2, 3, 4]): would return [0, 2] (indices in sorted array).
    # To get original indices [1,2] for elements 2 and 4, we'd do:
    #   original_with_indices = sorted([(num, i) for i, num in enumerate([3,2,4])]) -> [(2,1), (3,0), (4,2)]
    #   Apply two_pointer to this structure, comparing original_with_indices[left][0] + original_with_indices[right][0]
    #   If sum is target, return [original_with_indices[left][1], original_with_indices[right][1]]
    # This is beyond the scope of `two_sum_jedi_sorted_array` but important for "Jedi" understanding.
    print("\n(End of examples, Jedi discussion notes above for context on original indices)")
