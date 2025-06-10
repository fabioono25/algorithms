# Data Structures/5-LinkedList/1-MergeTwoSortedLists.py
# Data Structures/5-LinkedList/1-MergeTwoSortedLists.py
# Problem: You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by
# splicing together the nodes of the first two lists.

from typing import List, Optional # Adding Optional for ListNode.next type hint

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Helper function to print list (for testing)
    def __str__(self):
        vals = []
        curr = self
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        return " -> ".join(vals) if vals else "None"

# --- Simple Solution: Recursive Approach ---
def merge_two_lists_simple_recursive(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Merges two sorted linked lists recursively.
    Time Complexity: O(N + M), where N and M are the lengths of list1 and list2.
                     Each node is visited once.
    Space Complexity: O(N + M) due to recursion call stack in the worst case
                      (e.g., one list is much longer or elements are highly interleaved).
    Args:
        list1: The head of the first sorted linked list.
        list2: The head of the second sorted linked list.
    Returns:
        The head of the merged sorted linked list.
    """
    # Base cases
    if not list1:
        return list2
    if not list2:
        return list1

    # Recursive step
    if list1.val <= list2.val:
        merged_head = list1
        merged_head.next = merge_two_lists_simple_recursive(list1.next, list2)
        return merged_head
    else:
        merged_head = list2
        merged_head.next = merge_two_lists_simple_recursive(list1, list2.next)
        return merged_head

# --- Robust Solution: Iterative Approach with Dummy Head ---
def merge_two_lists_robust_iterative(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Merges two sorted linked lists iteratively using a dummy head node.
    Time Complexity: O(N + M). Each node is visited once.
    Space Complexity: O(1) (constant extra space for pointers and dummy node).
    Args:
        list1: The head of the first sorted linked list.
        list2: The head of the second sorted linked list.
    Returns:
        The head of the merged sorted linked list.
    """
    # Dummy head node to simplify edge cases (e.g., empty result list initially)
    dummy_head = ListNode(-1)
    current_tail = dummy_head # Points to the last node of the merged list

    p1, p2 = list1, list2 # Pointers for list1 and list2

    while p1 and p2:
        if p1.val <= p2.val:
            current_tail.next = p1
            p1 = p1.next
        else:
            current_tail.next = p2
            p2 = p2.next
        current_tail = current_tail.next

    # Append any remaining nodes from list1 or list2
    if p1:
        current_tail.next = p1
    elif p2:
        current_tail.next = p2

    return dummy_head.next # The merged list starts after the dummy head

# --- Jedi Solution: Analysis and Considerations ---
# (This section is primarily comments)

# **1. Time and Space Complexity:**
#    - **Recursive (Simple Solution):**
#        - Time: O(N+M). We visit each node from both lists once to decide its place.
#        - Space: O(N+M) in the worst case for the recursion call stack. This happens if
#          the lists are merged in a way that one call is made for almost every node (e.g.,
#          list1 = [1], list2 = [2,3,4,5,...]). If one list is exhausted quickly, the depth
#          is less.
#    - **Iterative (Robust Solution):**
#        - Time: O(N+M). We iterate through both lists once.
#        - Space: O(1). We only use a few pointers (`dummy_head`, `current_tail`, `p1`, `p2`).

# **2. Dummy Head Node Technique (Iterative Approach):**
#    - Using a `dummy_head` node is a common and very useful trick in linked list problems.
#    - Benefits:
#        - It simplifies the initialization of the merged list. Without it, you'd need
#          to handle the first node assignment as a special case.
#        - The `current_tail` pointer can always safely do `current_tail.next = ...`
#          because `dummy_head` ensures `current_tail` is never None initially.
#        - The final result is simply `dummy_head.next`.

# **3. In-Place vs. New List:**
#    - Both solutions presented modify the `next` pointers of the original nodes to form
#      the new merged list. They don't create new `ListNode` objects for each element
#      but rather rearrange existing ones. This is often what's implied by "splicing
#      together the nodes."
#    - If the problem required creating entirely new nodes for the merged list (leaving
#      original lists intact), the logic would involve creating `ListNode(val)` for each
#      element.

# **4. Variations:**
#    - **Merging k Sorted Lists:** This is a common follow-up problem.
#        - Approaches include:
#            - Repeatedly merging two lists at a time (O(k*TotalNodes) if TotalNodes is sum of all lengths).
#            - Using a min-heap to keep track of the smallest element among the heads of all
#              k lists (O(TotalNodes * log k)). This is generally more efficient for larger k.

# --- Example Usage ---
# Helper function to create a linked list from a Python list
def create_linked_list(values: List[int]) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

if __name__ == "__main__":
    print("--- Merge Two Sorted Lists ---")

    # Test Case 1
    l1_vals_tc1 = [1, 2, 4]
    l2_vals_tc1 = [1, 3, 4]
    # For creating fresh lists for each call
    def get_tc1_lists():
        return create_linked_list(l1_vals_tc1), create_linked_list(l2_vals_tc1)

    list1_disp, list2_disp = get_tc1_lists()
    print(f"\nTest Case 1:")
    print(f"List1: {list1_disp}")
    print(f"List2: {list2_disp}")

    list1_simple_tc1, list2_simple_tc1 = get_tc1_lists()
    merged_simple_tc1 = merge_two_lists_simple_recursive(list1_simple_tc1, list2_simple_tc1)
    print(f"Simple Recursive Merged: {merged_simple_tc1}") # Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4

    list1_robust_tc1, list2_robust_tc1 = get_tc1_lists()
    merged_robust_tc1 = merge_two_lists_robust_iterative(list1_robust_tc1, list2_robust_tc1)
    print(f"Robust Iterative Merged: {merged_robust_tc1}") # Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4

    # Test Case 2: One list is empty
    l1_vals_tc2 = []
    l2_vals_tc2 = [0]
    def get_tc2_lists():
        return create_linked_list(l1_vals_tc2), create_linked_list(l2_vals_tc2)

    list1_disp_tc2, list2_disp_tc2 = get_tc2_lists()
    print(f"\nTest Case 2:")
    print(f"List1: {list1_disp_tc2}")
    print(f"List2: {list2_disp_tc2}")

    list1_simple_tc2, list2_simple_tc2 = get_tc2_lists()
    merged_simple_tc2 = merge_two_lists_simple_recursive(list1_simple_tc2, list2_simple_tc2)
    print(f"Simple Recursive Merged (one empty): {merged_simple_tc2}") # Expected: 0

    list1_robust_tc2, list2_robust_tc2 = get_tc2_lists()
    merged_robust_tc2 = merge_two_lists_robust_iterative(list1_robust_tc2, list2_robust_tc2)
    print(f"Robust Iterative Merged (one empty): {merged_robust_tc2}") # Expected: 0

    # Test Case 3: Both lists are empty
    print(f"\nTest Case 3:")
    print(f"List1: None")
    print(f"List2: None")
    merged_simple_tc3 = merge_two_lists_simple_recursive(None, None)
    print(f"Simple Recursive Merged (both empty): {merged_simple_tc3}") # Expected: None
    merged_robust_tc3 = merge_two_lists_robust_iterative(None, None)
    print(f"Robust Iterative Merged (both empty): {merged_robust_tc3}") # Expected: None

    print("\nJedi Solution (Discussion): See comments in code.")

# Typing import for the helper function
# from typing import List # Moved to the top