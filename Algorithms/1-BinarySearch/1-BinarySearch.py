# Simple Solution
# here is a simple implementation of Binary Search

def binary_search(list, item):
  low = 0
  high = len(list) - 1

  while low <= high:
    mid = (low + high) // 2
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return None


# Robust Solution
def binary_search_recursive(arr, low, high, item):
    """
    Recursive implementation of binary search.

    Args:
        arr: A sorted list of elements.
        low: The starting index for the search.
        high: The ending index for the search.
        item: The item to search for.

    Returns:
        The index of the item if found, otherwise None.
    """
    # Base case: If the search space is invalid (low > high),
    # the item is not in the list.
    if high >= low:
        mid = low + (high - low) // 2  # Calculate mid point

        # If the middle element is the item, return its index.
        if arr[mid] == item:
            return mid
        # If the item is smaller than the middle element,
        # it can only be present in the left subarray.
        elif arr[mid] > item:
            return binary_search_recursive(arr, low, mid - 1, item)
        # Else the item can only be present in the right subarray.
        else:
            return binary_search_recursive(arr, mid + 1, high, item)
    else:
        # Item is not present in the array
        return None

# Note on handling multiple occurrences:
# Standard binary search (both iterative and this recursive version) typically returns
# the first instance of the target it finds. If the list can have duplicates
# and you need to find the *very first* or *last* occurrence, the algorithm
# needs modification. For example, after finding an item, you could continue
# searching in the left part of the array to find an earlier occurrence.


# Jedi Solution
import bisect

def binary_search_bisect(arr, item):
    """
    Implements binary search using the bisect_left function from the bisect module.

    Args:
        arr: A sorted list of elements.
        item: The item to search for.

    Returns:
        The index of the item if found, otherwise indicates where it would be inserted
        (and by checking the value at that index, if it's the item).
        Returns a string "Item not found" if not present.
    """
    # bisect_left returns an insertion point which comes before (to the left of) any
    # existing entries of item in arr and after (to the right of) any existing
    # entries of item in arr.
    # If item is already present in arr, the insertion point will be before (to the left of)
    # the first occurrence of item.
    index = bisect.bisect_left(arr, item)

    # Check if the item was found
    # 1. The index must be within the bounds of the array.
    # 2. The element at the found index must be equal to the item.
    if index < len(arr) and arr[index] == item:
        return index  # Item found at this index
    else:
        # Item not found. The 'index' variable still holds the position
        # where 'item' would be inserted to maintain sort order.
        return "Item not found"

# Example Usage (original examples + new ones for robust and Jedi solutions)
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print("# Simple Solution Examples:")
print(f"Searching for 3: Index {binary_search(my_list, 3)}") # => 1
print(f"Searching for -1: {binary_search(my_list, -1)}")    # => None
print(f"Searching for 19: Index {binary_search(my_list, 19)}")# => 9
print(f"Searching for 10: {binary_search(my_list, 10)}")   # => None

print("\n# Robust Solution Examples (Recursive):")
print(f"Searching for 7: Index {binary_search_recursive(my_list, 0, len(my_list)-1, 7)}")  # => 3
print(f"Searching for 1: Index {binary_search_recursive(my_list, 0, len(my_list)-1, 1)}")  # => 0
print(f"Searching for 19: Index {binary_search_recursive(my_list, 0, len(my_list)-1, 19)}") # => 9
print(f"Searching for 0: {binary_search_recursive(my_list, 0, len(my_list)-1, 0)}")     # => None
print(f"Searching for 20: {binary_search_recursive(my_list, 0, len(my_list)-1, 20)}")    # => None
# Example with an empty list
empty_list = []
print(f"Searching for 5 in empty list: {binary_search_recursive(empty_list, 0, len(empty_list)-1, 5)}") # => None

print("\n# Jedi Solution Examples (bisect_left):")
print(f"Searching for 11: Index {binary_search_bisect(my_list, 11)}") # => 5
print(f"Searching for 1: Index {binary_search_bisect(my_list, 1)}")   # => 0
print(f"Searching for 19: Index {binary_search_bisect(my_list, 19)}")  # => 9
print(f"Searching for 6: {binary_search_bisect(my_list, 6)}")      # => Item not found
print(f"Searching for 25: {binary_search_bisect(my_list, 25)}")     # => Item not found
print(f"Searching for 0: {binary_search_bisect(my_list, 0)}")      # => Item not found
# Example with an empty list
print(f"Searching for 5 in empty list: {binary_search_bisect(empty_list, 5)}") # => Item not found

# Example with duplicates to illustrate bisect_left behavior
duplicate_list = [2, 4, 4, 4, 6, 8]
print(f"Searching for 4 in {duplicate_list}: Index {binary_search_bisect(duplicate_list, 4)}") # => 1 (index of the first 4)
print(f"Searching for 3 in {duplicate_list}: {binary_search_bisect(duplicate_list, 3)}")   # => Item not found (bisect_left would return 1)
print(f"Searching for 5 in {duplicate_list}: {binary_search_bisect(duplicate_list, 5)}")   # => Item not found (bisect_left would return 4)
