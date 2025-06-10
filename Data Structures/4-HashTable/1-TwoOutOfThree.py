# Data Structures/4-HashTable/1-TwoOutOfThree.py
# Problem: Given three integer arrays nums1, nums2, and nums3, return a distinct
#          array containing all the values that are present in at least
#          two out of the three arrays. You may return the values in any order.

from typing import List
from collections import Counter # For an alternative Jedi approach

# --- Simple Solution: Iterative Checking with List ---
def two_out_of_three_simple(nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
    """
    Finds numbers present in at least two of the three lists using basic iteration
    and list lookups for uniqueness. This version iterates through all unique numbers
    from all lists and counts their presence in sets derived from the input lists.
    Time Complexity: O(L1+L2+L3) for set conversions. Then, for U unique numbers across all lists,
                     it's O(U * (1+1+1)) for set lookups. So, roughly O(L1+L2+L3).
    Space Complexity: O(U1+U2+U3) for storing the sets, where Ui is unique elements in nums_i.
                      Plus O(K) for the result list, where K is the number of unique results.
    """
    set1, set2, set3 = set(nums1), set(nums2), set(nums3)
    result = []

    # Combine all unique numbers from all three sets
    all_unique_nums = set1.union(set2).union(set3)

    for num in all_unique_nums:
        count = 0
        if num in set1:
            count += 1
        if num in set2:
            count += 1
        if num in set3:
            count += 1

        if count >= 2:
            # The check `num not in result` is not needed here because we are iterating
            # over `all_unique_nums`, so each number is considered only once for addition.
            result.append(num)

    return result


# --- Robust Solution: Using a HashMap (Dictionary) for Counting ---
# (Based on the original `TwoOutOfThree` function logic)
def two_out_of_three_robust_map(nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
    """
    Uses a hash map to count the occurrences of each number across the unique
    elements of the three input arrays. Each number increments its count in the map
    only once per list it appears in.
    Time Complexity: O(L1 + L2 + L3) on average, where Li is the length of nums_i
                     (for converting lists to sets and then iterating these sets).
    Space Complexity: O(U1 + U2 + U3) for the sets and O(U_total) for the hash map,
                      where Ui is unique elements in nums_i and U_total is total unique elements.
                      So, roughly O(L1+L2+L3) in worst case if all elements are unique.
    """
    counts_map = {} # Using a dictionary as a hash map/frequency counter

    # Process unique elements from each list
    # For each number, mark its presence in list 1, 2, or 3.
    # A number appearing multiple times in one list still counts as one appearance for that list.
    for num in set(nums1):
        counts_map[num] = counts_map.get(num, 0) + 1
    for num in set(nums2):
        counts_map[num] = counts_map.get(num, 0) + 1
    for num in set(nums3):
        counts_map[num] = counts_map.get(num, 0) + 1

    result = []
    for num, count in counts_map.items():
        if count >= 2: # If the number appeared in at least 2 of the sets
            result.append(num)
    return result

# --- Jedi Solution: Leveraging Sets for Concise Logic & Counter ---
# (Set logic based on the original `TwoOutOfThree2` function, but more direct)
def two_out_of_three_jedi_sets(nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
    """
    Leverages Python sets and their intersection/union properties for a concise solution.
    Time Complexity: O(L1 + L2 + L3) on average (due to set conversions and operations).
                     Length of lists dominates set operation time.
    Space Complexity: O(U1 + U2 + U3) in the worst case for storing sets, where Ui is
                      the number of unique elements in nums_i.
    """
    s1, s2, s3 = set(nums1), set(nums2), set(nums3)

    # Elements in (s1 and s2) OR (s1 and s3) OR (s2 and s3)
    # This directly finds numbers that are in at least two of the sets.
    # s1 & s2: in nums1 and nums2
    # s1 & s3: in nums1 and nums3
    # s2 & s3: in nums2 and nums3
    # Union of these gives all numbers present in at least two sets.
    result_set = (s1.intersection(s2)) \
               | (s1.intersection(s3)) \
               | (s2.intersection(s3))

    return list(result_set)

# **Alternative Jedi Solution (using collections.Counter on set flags):**
def two_out_of_three_jedi_counter(nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
    """
    Uses collections.Counter to count how many sets each number appears in.
    This is similar to the robust_map solution but uses `collections.Counter`.
    Time Complexity: O(L1+L2+L3) for set conversions and iterations.
    Space Complexity: O(U1+U2+U3) for sets and Counter.
    """
    # Using sets ensures each number from a list contributes at most once to its list's count
    s1, s2, s3 = set(nums1), set(nums2), set(nums3)

    counts = Counter()
    # Increment count for each number found in each set
    for x in s1: counts[x] += 1
    for x in s2: counts[x] += 1
    for x in s3: counts[x] += 1

    # Select numbers that appeared in 2 or more sets
    return [x for x, count_val in counts.items() if count_val >= 2]


# --- Example Usage ---
if __name__ == "__main__":
    print("--- Two Out Of Three ---")
    test_cases = [
        ([1,1,3,2], [2,3], [3], [2,3]),
        ([3,1], [2,3], [1,2], [1,2,3]),
        ([1,2,2], [4,3,3], [5], []),
        ([7,7,7,7], [7,7,7,7], [7,7,7,7], [7]), # All same, multiple times
        ([1,5], [2,5], [3,5], [5]),           # One common across all three
        ([1,2], [2,3], [3,1], [1,2,3])        # Pairwise common
    ]

    for i, (n1, n2, n3, expected) in enumerate(test_cases):
        print(f"\nTest Case {i+1}:")
        print(f"  Lists: {n1}, {n2}, {n3}")
        print(f"  Expected: {sorted(expected)}")

        res_simple = sorted(two_out_of_three_simple(list(n1), list(n2), list(n3)))
        print(f"  Simple:         {res_simple} {'OK' if res_simple == sorted(expected) else 'FAIL'}")

        res_robust_map = sorted(two_out_of_three_robust_map(list(n1), list(n2), list(n3)))
        print(f"  Robust (Map):   {res_robust_map} {'OK' if res_robust_map == sorted(expected) else 'FAIL'}")

        res_jedi_sets = sorted(two_out_of_three_jedi_sets(list(n1), list(n2), list(n3)))
        print(f"  Jedi (Sets):    {res_jedi_sets} {'OK' if res_jedi_sets == sorted(expected) else 'FAIL'}")

        res_jedi_counter = sorted(two_out_of_three_jedi_counter(list(n1), list(n2), list(n3)))
        print(f"  Jedi (Counter): {res_jedi_counter} {'OK' if res_jedi_counter == sorted(expected) else 'FAIL'}")