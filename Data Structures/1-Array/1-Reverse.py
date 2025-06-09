# Data Structures/1-Array/1-Reverse.py

# Problem: Reverse an array (or a Python list).

# --- Simple Solution: Python Slicing (Out-of-Place) ---
def reverse_array_simple(arr):
    """
    Reverses an array using Python's slicing feature.
    This creates a new reversed copy of the array (out-of-place).
    Args:
        arr (list): The input array (list).
    Returns:
        list: A new list containing elements of arr in reverse order.
              Returns an empty list if input is empty.
    """
    if not arr:
        return []
    return arr[::-1]

# --- Robust Solution: Two-Pointer In-Place Reversal ---
def reverse_array_robust_inplace(arr):
    """
    Reverses an array in-place using the two-pointer technique.
    Modifies the original array directly.
    Args:
        arr (list): The input array (list). This list will be modified.
    Returns:
        None: The function modifies the list in-place.
    """
    if not arr:
        return

    low = 0
    high = len(arr) - 1
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
    # No explicit return needed as the original list is modified.

# --- Jedi Solution: Analysis, Built-in Methods, and Considerations ---
# (This section is primarily comments and discussion)

# **Analysis:**
# 1. Simple Solution (Slicing `arr[::-1]`):
#    - Time Complexity: O(N), where N is the number of elements in the array.
#      A new list is created, and all elements are copied.
#    - Space Complexity: O(N), as a new list of N elements is created.
#    - Pythonic and very readable for creating a reversed copy.

# 2. Robust Solution (Two-Pointer In-Place):
#    - Time Complexity: O(N), as it iterates through roughly N/2 elements for swapping.
#    - Space Complexity: O(1) (constant extra space), as the reversal happens in-place.
#    - Ideal when memory is a concern or the original list needs to be modified directly.

# **Python's Built-in `list.reverse()` method:**
# Python lists have a built-in `reverse()` method that reverses the list in-place.
# Example:
#   my_list = [1, 2, 3, 4]
#   my_list.reverse()  # my_list becomes [4, 3, 2, 1]
# This method is implemented in C and is highly optimized, usually the preferred way
# for in-place reversal of actual Python lists. It also has O(N) time and O(1) space.

# **Reversing other sequence types:**
# - For tuples or strings (immutable sequences), slicing `[::-1]` is the standard way
#   to get a reversed version (always a new object).
# - For custom list-like objects, the feasibility and efficiency of in-place reversal
#   would depend on the object's internal structure and supported operations (e.g.,
#   does it support efficient item assignment and length determination?).

# **Considerations for iterators/generators:**
# If you have an iterator or generator and need to reverse it, you typically need to
# first convert it to a concrete sequence (like a list), then reverse that.
# Example: list(reversed(my_iterator)) or list(my_iterator)[::-1]
# The `reversed()` built-in function returns a reverse iterator.

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Reverse an Array ---")

    # Test Simple Solution
    print("\nSimple Solution (Slicing):")
    list1 = [1, 2, 3, 4, 5]
    print(f"Original: {list1}, Reversed copy: {reverse_array_simple(list1)}")
    list_empty_simple = []
    print(f"Original empty: {list_empty_simple}, Reversed copy: {reverse_array_simple(list_empty_simple)}")

    # Test Robust Solution
    print("\nRobust Solution (In-Place Two-Pointer):")
    list2 = [1, 2, 3, 4, 5, 6]
    print(f"Original: {list2}")
    reverse_array_robust_inplace(list2)
    print(f"Reversed in-place: {list2}")

    list3 = ['a', 'b', 'c']
    print(f"Original: {list3}")
    reverse_array_robust_inplace(list3)
    print(f"Reversed in-place: {list3}")

    list_empty_robust = []
    print(f"Original empty: {list_empty_robust}")
    reverse_array_robust_inplace(list_empty_robust)
    print(f"Reversed in-place: {list_empty_robust}")


    # Demonstrate Jedi discussion points
    print("\nJedi Solution (Built-in list.reverse()):")
    list4 = [10, 20, 30, 40]
    print(f"Original: {list4}")
    list4.reverse() # Using the built-in method
    print(f"Reversed using list.reverse(): {list4}")

    print("\nJedi Solution (reversed() with iterators/strings):")
    my_string = "hello"
    reversed_string = "".join(list(reversed(my_string))) # or my_string[::-1]
    print(f"Original string: '{my_string}', Reversed string: '{reversed_string}'")

    my_tuple = (1, 2, 3)
    reversed_tuple_iter = reversed(my_tuple) # returns a reverse iterator
    print(f"Original tuple: {my_tuple}, Reversed via iterator: {list(reversed_tuple_iter)}")
