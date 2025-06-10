# Data Structures/5-LinkedList/0-SimpleLinkedList.py
# Problem: Implement a Singly Linked List from scratch.
# This will include Node class, and LinkedList class with common operations.

# --- Node Class ---
class Node:
    """
    Represents a single node in a singly linked list.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

# --- Simple Solution: Basic LinkedList with Append, Prepend, Display ---
class SimpleLinkedList:
    """
    A basic implementation of a Singly Linked List.
    Supports append, prepend, and display operations.
    """
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def append(self, data) -> None:
        """Appends a new node with data to the end of the list. O(N) without tail pointer."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data) -> None:
        """Prepends a new node with data to the beginning of the list. O(1)."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self, as_list=False):
        """Prints the linked list elements or returns them as a Python list."""
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next

        if as_list:
            return elements
        else:
            print(" -> ".join(map(str, elements)) if elements else "None (Empty List)")

# --- Robust Solution: LinkedList with Delete, Search, Insert After ---
class RobustLinkedList(SimpleLinkedList): # Inherits from SimpleLinkedList
    """
    Extends SimpleLinkedList with more operations:
    - delete(key): Deletes the first occurrence of a node with the given key.
    - search(key): Searches for a node with the given key and returns the node or None.
    - insert_after_node_data(prev_node_data, new_data): Inserts a new node after a node with specific data.
    - Tracks size.
    - Uses a tail pointer for O(1) append.
    """
    def __init__(self):
        super().__init__()
        self.tail = None # Add a tail pointer
        self.num_elements = 0

    # Override append for O(1) complexity using tail pointer
    def append(self, data) -> None:
        """Appends a new node with data to the end of the list. O(1) with tail pointer."""
        new_node = Node(data)
        if self.is_empty(): # self.head is None
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.num_elements += 1

    # Override prepend to update tail if list was empty, and num_elements
    def prepend(self, data) -> None:
        """Prepends a new node with data to the beginning of the list. O(1)."""
        new_node = Node(data)
        if self.is_empty(): # self.head is None
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def delete(self, key_to_delete) -> bool:
        """
        Deletes the first node containing the 'key_to_delete'.
        Returns True if deletion was successful, False otherwise.
        Handles head deletion and updates tail if the last node is deleted.
        Time Complexity: O(N) in worst case (searching for the key).
        """
        if self.is_empty():
            return False

        current = self.head
        prev = None

        # Case 1: Deleting the head node
        if current.data == key_to_delete:
            self.head = current.next
            if self.head is None: # List became empty
                self.tail = None
            self.num_elements -=1
            # current.next = None # Optional: clean up deleted node's pointer
            return True

        # Case 2: Deleting a node other than the head
        while current and current.data != key_to_delete:
            prev = current
            current = current.next

        if current is None: # Key not found
            return False

        # Unlink the node: prev points to current's next
        prev.next = current.next
        if prev.next is None: # If the deleted node (current) was the tail
            self.tail = prev   # The new tail is prev
        # current.next = None # Optional: clean up deleted node's pointer
        self.num_elements -=1
        return True

    def search(self, key_to_find) -> Node:
        """
        Searches for the first node containing 'key_to_find'.
        Returns the Node object if found, otherwise None.
        Time Complexity: O(N).
        """
        current = self.head
        while current:
            if current.data == key_to_find:
                return current
            current = current.next
        return None

    def insert_after_node_data(self, prev_node_data, data_to_insert) -> bool:
        """
        Inserts a new node with 'data_to_insert' after the first node
        that has 'prev_node_data'.
        Returns True if successful, False if prev_node_data is not found.
        Time Complexity: O(N) for searching prev_node.
        """
        prev_node_found = self.search(prev_node_data)
        if not prev_node_found:
            print(f"Error: Node with data '{prev_node_data}' not found.")
            return False

        new_node = Node(data_to_insert)
        new_node.next = prev_node_found.next
        prev_node_found.next = new_node
        if new_node.next is None: # If inserting after the current tail
            self.tail = new_node
        self.num_elements += 1
        return True

    def get_size(self) -> int:
        return self.num_elements


# --- Jedi Solution: Discussion of Advanced Concepts & Dummy Head ---
# (This section is primarily comments)

# **1. Complexities of Operations (RobustLinkedList with tail pointer):**
#    - `append(data)`: O(1) - Thanks to the tail pointer.
#    - `prepend(data)`: O(1) - Modifies head.
#    - `delete(key)`: O(N) - Involves searching for the key. O(1) if deleting head (if key is at head).
#    - `search(key)`: O(N) - Linear scan.
#    - `insert_after_node_data(prev_data, new_data)`: O(N) - Due to search for `prev_data`.
#      (If `prev_node` object was given, it would be O(1) to insert after it).
#    - `get_size()`: O(1) - If size is tracked. O(N) if iterated.
#    - Space Complexity: O(N) for storing N nodes.

# **2. Dummy Head Node (Sentinel Node):**
#    - A dummy head node is a placeholder node at the beginning of the list that
#      doesn't store actual data (or stores a sentinel value).
#    - Benefits:
#        - Simplifies insertion and deletion logic, especially at the head of the list.
#          You no longer need special `if self.head == ...` conditions
#          directly within `delete` or `insert_at_beginning` if structured carefully.
#          For example, `prev` pointer in delete would always point to a valid node (the dummy)
#          if the actual list starts after the dummy.
#        - The list is never "truly" empty from the perspective of pointer manipulation
#          (it always has the dummy head). `self.head` would point to dummy, and the
#          actual list starts at `dummy.next`.
#    - Example: `self.head = Node()` (dummy), and all operations work off `self.head.next`.
#      The `append` and `prepend` in `RobustLinkedList` would need slight adjustments
#      if a dummy head was used (e.g. tail would never be None, it would be the dummy if empty).

# **3. Doubly Linked Lists:**
#    - Each node has `data`, `next` pointer, AND a `prev` (previous) pointer.
#    - Advantages:
#        - Can traverse backwards.
#        - Deletion can be O(1) if you have a direct pointer to the node to be deleted
#          (no need to find `prev` node by iterating from head, as `node_to_delete.prev` is available).
#    - Disadvantages:
#        - More memory per node (for `prev` pointer).
#        - Insertions and deletions are slightly more complex as more pointers need updating (both `next` and `prev`).

# **4. Circular Linked Lists:**
#    - The `next` pointer of the last node points back to the head node (or a dummy head)
#      instead of `None`.
#    - Useful for round-robin type algorithms, managing circular buffers, etc.
#    - Traversal needs care to avoid infinite loops (e.g., stop when back at head, or use a counter).

# **5. Python's Built-in Data Structures:**
#    - While implementing linked lists is a great learning exercise, Python's `list`
#      (dynamic array) is often more practical for general sequences due to cache
#      efficiency and optimized C implementation for many operations.
#    - `collections.deque` is excellent for O(1) appends and pops from both ends,
#      making it suitable for stacks and queues. It's implemented as a doubly linked list
#      of blocks of arrays, offering good performance characteristics for list-like operations
#      at both ends.

# --- Example Usage ---
if __name__ == "__main__":
    print("--- SimpleLinkedList ---")
    sll = SimpleLinkedList()
    sll.display() # None (Empty List)
    sll.append(10)
    sll.append(20)
    sll.prepend(5) # 5 -> 10 -> 20
    sll.display()
    print(f"As list: {sll.display(as_list=True)}")

    print("\n--- RobustLinkedList ---")
    rll = RobustLinkedList()
    rll.append(100) # Head: 100, Tail: 100, Size: 1
    rll.display()
    print(f"Size: {rll.get_size()}, Head: {rll.head.data if rll.head else 'None'}, Tail: {rll.tail.data if rll.tail else 'None'}")

    rll.append(200) # Head: 100, Tail: 200, Size: 2. List: 100 -> 200
    rll.display()
    print(f"Size: {rll.get_size()}, Head: {rll.head.data if rll.head else 'None'}, Tail: {rll.tail.data if rll.tail else 'None'}")

    rll.prepend(50) # Head: 50, Tail: 200, Size: 3. List: 50 -> 100 -> 200
    rll.display()
    print(f"Size: {rll.get_size()}, Head: {rll.head.data if rll.head else 'None'}, Tail: {rll.tail.data if rll.tail else 'None'}")

    rll.insert_after_node_data(100, 150) # 50 -> 100 -> 150 -> 200. Tail: 200, Size: 4
    rll.display()
    print(f"Size: {rll.get_size()}, Head: {rll.head.data if rll.head else 'None'}, Tail: {rll.tail.data if rll.tail else 'None'}")

    rll.insert_after_node_data(200, 250) # Insert after tail: 50 -> 100 -> 150 -> 200 -> 250. Tail becomes 250. Size: 5
    rll.display()
    print(f"Size: {rll.get_size()}, Head: {rll.head.data if rll.head else 'None'}, Tail: {rll.tail.data if rll.tail else 'None'}")

    print(f"Search for 150: Node data is {rll.search(150)}") # Node data is 150
    print(f"Search for 999: {rll.search(999)}")      # None

    rll.delete(50) # Delete head: 100 -> 150 -> 200 -> 250. Tail: 250, Size: 4
    rll.display()
    print(f"Size: {rll.get_size()}, Head: {rll.head.data if rll.head else 'None'}, Tail: {rll.tail.data if rll.tail else 'None'}")

    rll.delete(200) # 100 -> 150 -> 250. Tail: 250, Size: 3
    rll.display()
    print(f"Size: {rll.get_size()}, Head: {rll.head.data if rll.head else 'None'}, Tail: {rll.tail.data if rll.tail else 'None'}")

    rll.delete(250) # Delete tail: 100 -> 150. Tail becomes 150. Size: 2
    rll.display()
    print(f"Size: {rll.get_size()}, Head: {rll.head.data if rll.head else 'None'}, Tail: {rll.tail.data if rll.tail else 'None'}")

    rll.delete(100) # 150. Tail: 150, Size: 1
    rll.display()
    print(f"Size: {rll.get_size()}, Head: {rll.head.data if rll.head else 'None'}, Tail: {rll.tail.data if rll.tail else 'None'}")

    rll.delete(150) # List becomes empty. Tail: None, Size: 0
    rll.display() # None (Empty List)
    print(f"Size: {rll.get_size()}, Head: {rll.head.data if rll.head else 'None'}, Tail: {rll.tail.data if rll.tail else 'None'}")

    print(f"Delete from empty list: {rll.delete(10)}") # False

    print("\n--- Jedi Solution (Discussion) ---")
    print("See comments in the Jedi Solution section for details on advanced concepts.")
