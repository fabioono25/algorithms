# Data Structures/1-Array/10-MedianOfTwoSortedArrays.py
# Problem: Given two sorted arrays nums1 and nums2 of size m and n respectively,
#          return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)) for the optimal solution.

from typing import List

# --- Simple Solution: Merge and Find Median ---
def median_simple_merge(nums1: List[int], nums2: List[int]) -> float:
    """
    Finds the median of two sorted arrays by first merging them into a single sorted array.
    Time Complexity: O(m+n) for merging.
    Space Complexity: O(m+n) for the merged array.
    Args:
        nums1: First sorted list of integers.
        nums2: Second sorted list of integers.
    Returns:
        The median of the combined sorted lists.
    """
    merged = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    # Append remaining elements
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])

    total_len = len(merged)
    if total_len == 0:
        return 0.0 # Or raise error, depending on problem spec for empty inputs

    mid_idx = total_len // 2
    if total_len % 2 == 1: # Odd number of elements
        return float(merged[mid_idx])
    else: # Even number of elements
        # For even length, median is avg of elements at mid-1 and mid
        return (merged[mid_idx - 1] + merged[mid_idx]) / 2.0

# --- Robust Solution: Iterative Median Search (Constant Space) ---
def median_robust_iterative(nums1: List[int], nums2: List[int]) -> float:
    """
    Finds the median by iterating up to the middle element(s) of the combined array
    without actually merging the entire arrays. Simulates the merge process.
    Time Complexity: O(m+n) - in the worst case, iterates through (m+n)/2 elements.
                     More accurately, O((m+n)/2 + 1) steps.
    Space Complexity: O(1) - only a few variables to keep track of current elements.
    Args:
        nums1: First sorted list of integers.
        nums2: Second sorted list of integers.
    Returns:
        The median of the combined sorted lists.
    """
    m, n = len(nums1), len(nums2)
    total_len = m + n
    if total_len == 0:
        return 0.0

    # Variables to store the two elements around the median
    # m1 is for element at index (total_len // 2) - 1 if total_len is even
    # m2 is for element at index (total_len // 2)
    m1, m2 = -1.0, -1.0
    
    # Indices for iterating through nums1 and nums2
    i, j = 0, 0

    # We need to find up to (total_len // 2)-th element (0-indexed)
    # So we iterate (total_len // 2) + 1 times.
    for count in range((total_len // 2) + 1):
        m1 = m2 # Store the previous m2, which becomes m1 for the current step
        if i < m and j < n:
            if nums1[i] < nums2[j]:
                m2 = float(nums1[i])
                i += 1
            else:
                m2 = float(nums2[j])
                j += 1
        elif i < m: # nums2 is exhausted
            m2 = float(nums1[i])
            i += 1
        else: # nums1 is exhausted (j must be < n)
            m2 = float(nums2[j])
            j += 1
    
    if total_len % 2 == 1: # Odd total length, median is the middle element
        return m2
    else: # Even total length, median is average of the two middle elements
        return (m1 + m2) / 2.0

# --- Jedi Solution: Binary Search on Partitions ---
# (This is based on the original highly optimized solution from prompt, adapted and commented)
def median_jedi_binary_search(nums1: List[int], nums2: List[int]) -> float:
    """
    Finds the median of two sorted arrays using a binary search approach on partitions.
    This method aims for O(log(min(m,n))) time complexity.
    The core idea is to partition both arrays such that all elements in the "left"
    combined partition are less than or equal to all elements in the "right" combined partition.
    The median will be derived from the boundary elements of these partitions.

    Args:
        nums1: First sorted list of integers.
        nums2: Second sorted list of integers.
    Returns:
        The median of the combined sorted lists.
    """
    m, n = len(nums1), len(nums2)

    # Ensure nums1 is the smaller array (or equal) for binary search efficiency.
    # The binary search will be on the partitions of the smaller array.
    if m > n:
        return median_jedi_binary_search(nums2, nums1) # Swap arrays

    # Handle edge cases with empty arrays
    if m == 0 and n == 0: # Both empty
        return 0.0 # Or raise an error as per problem specification
    if m == 0: # nums1 is empty, median is from nums2
        mid_n = n // 2
        return float(nums2[mid_n]) if n % 2 == 1 else (nums2[mid_n - 1] + nums2[mid_n]) / 2.0
    # If m != 0, then n cannot be 0 here because if n was 0, m > n would have been true (m > 0, n = 0),
    # leading to a swap, and then it would have been caught by the m == 0 case.

    total_len = m + n
    # `half_len` is the count of elements that should be in the "left half"
    # of the conceptual merged array.
    # If total_len is odd (e.g., 5), half_len is 3. The median is the 3rd element (max of left half).
    # If total_len is even (e.g., 6), half_len is 3. Median is avg of 3rd and 4th elements
    # (max of left half and min of right half).
    half_len = (total_len + 1) // 2

    # Binary search for the correct partition in the smaller array (nums1).
    # `low` and `high` define the range for `partition1` (number of elements from nums1
    # in the left combined partition). `partition1` can range from 0 to m.
    low = 0
    high = m

    while low <= high:
        # `partition1` is the number of elements taken from `nums1` for the left partition.
        # It's also the cut point in `nums1` (0-indexed means elements nums1[0]...nums1[partition1-1]).
        partition1 = (low + high) // 2
        # `partition2` is the number of elements taken from `nums2` for the left partition.
        partition2 = half_len - partition1

        # Determine the four key elements around the conceptual cut:
        # max_left1: The largest element from nums1 in the left partition.
        # min_right1: The smallest element from nums1 in the right partition.
        # max_left2: The largest element from nums2 in the left partition.
        # min_right2: The smallest element from nums2 in the right partition.

        # If partition1 is 0, no elements from nums1 are in the left half, so max_left1 is -infinity.
        max_left1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
        # If partition1 is m, all elements from nums1 are in the left half, so min_right1 is +infinity.
        min_right1 = nums1[partition1] if partition1 < m else float('inf')
        
        max_left2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
        min_right2 = nums2[partition2] if partition2 < n else float('inf')

        # Check if the current partitions are correct:
        # The largest element in the left partition from nums1 must be <= smallest in right from nums2.
        # The largest element in the left partition from nums2 must be <= smallest in right from nums1.
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            # Correct partition found. Now calculate the median.
            if total_len % 2 == 1: # Odd total length
                # The median is the maximum of the elements at the end of the left partitions.
                return float(max(max_left1, max_left2))
            else: # Even total length
                # The median is the average of the maximum of the left partition elements
                # and the minimum of the right partition elements.
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
        elif max_left1 > min_right2:
            # `partition1` includes too large an element from `nums1`.
            # Need to move the cut in `nums1` to the left (reduce `partition1`).
            high = partition1 - 1
        else: # max_left2 > min_right1
            # `partition1` is too small.
            # Need to move the cut in `nums1` to the right (increase `partition1`).
            low = partition1 + 1

    return 0.0 # Should ideally not be reached if inputs are valid sorted arrays.

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Median of Two Sorted Arrays ---")

    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0,0], [0,0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([1,3,5,7,9], [2,4,6,8,10], 5.5),
        ([1,2,3,4,5], [6,7,8,9,10], 5.5), # Median between two arrays
        ([6,7,8,9,10], [1,2,3,4,5], 5.5), # Order swapped
        ([1], [2,3,4,5,6,7,8,9,10], 5.5), # Highly unbalanced
        ([2,3,4,5,6,7,8,9,10], [1], 5.5)  # Highly unbalanced swapped
    ]

    for nums1_ex, nums2_ex, target_ex in test_cases:
        print(f"\nNums1: {nums1_ex}, Nums2: {nums2_ex}, Expected: {target_ex}")
        # Pass copies to ensure original test case lists are not modified by any function
        print(f"Simple (Merge):       {median_simple_merge(list(nums1_ex), list(nums2_ex))}")
        print(f"Robust (Iterative):   {median_robust_iterative(list(nums1_ex), list(nums2_ex))}")
        print(f"Jedi (Binary Search): {median_jedi_binary_search(list(nums1_ex), list(nums2_ex))}")

    print("\nTesting with both empty arrays:")
    nums1_empty_both, nums2_empty_both = [], []
    target_empty_both = 0.0 # As per current implementation
    print(f"Nums1: {nums1_empty_both}, Nums2: {nums2_empty_both}, Expected: {target_empty_both}")
    print(f"Simple (Merge):       {median_simple_merge(list(nums1_empty_both), list(nums2_empty_both))}")
    print(f"Robust (Iterative):   {median_robust_iterative(list(nums1_empty_both), list(nums2_empty_both))}")
    print(f"Jedi (Binary Search): {median_jedi_binary_search(list(nums1_empty_both), list(nums2_empty_both))}")