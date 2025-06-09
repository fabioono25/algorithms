# Data Structures/2-Queue/1-QueueUsingStack.py
# Problem: Implement a FIFO queue using only two stacks.
# The implemented queue should support all the functions of a normal queue
# (enqueue, dequeue, peek, empty).

# Stacks in Python can be simulated using lists with append() for push and pop() for pop.
from collections import deque # Imported for Jedi section example

# --- Simple Solution: Dequeue is Costly ---
class MyQueueSimple:
    """
    Implements a queue using two stacks (`stack_enqueue` and `stack_dequeue_helper`).
    In this version, enqueue is O(1), but dequeue and peek can be O(N)
    as they may involve transferring all elements between stacks every time.
    This implementation is straightforward but less efficient for dequeue/peek.
    """
    def __init__(self):
        self.stack_enqueue = []  # Used for enqueue operations
        self.stack_dequeue_helper = [] # Used as a temporary helper for dequeue/peek

    def enqueue(self, x: int) -> None:
        """Pushes element x to the back of the queue. O(1)."""
        self.stack_enqueue.append(x)

    def dequeue(self) -> int:
        """
        Removes the element from the front of the queue and returns it. O(N).
        """
        if self.empty():
            raise IndexError("dequeue from empty queue")

        # Transfer all elements from stack_enqueue to stack_dequeue_helper
        # This reverses the order, so the front of the queue is at the top of helper.
        while self.stack_enqueue:
            self.stack_dequeue_helper.append(self.stack_enqueue.pop())

        # Pop the front element (which is now at the top of stack_dequeue_helper)
        front_element = self.stack_dequeue_helper.pop()

        # Transfer all elements back to stack_enqueue to maintain original enqueue order
        while self.stack_dequeue_helper:
            self.stack_enqueue.append(self.stack_dequeue_helper.pop())

        return front_element

    def peek(self) -> int:
        """
        Returns the element at the front of the queue. O(N).
        """
        if self.empty():
            raise IndexError("peek from empty queue")

        # Transfer to helper to find the front element
        while self.stack_enqueue:
            self.stack_dequeue_helper.append(self.stack_enqueue.pop())

        # The front element is now at the top of stack_dequeue_helper
        front_element = self.stack_dequeue_helper[-1]

        # Transfer back
        while self.stack_dequeue_helper:
            self.stack_enqueue.append(self.stack_dequeue_helper.pop())

        return front_element

    def empty(self) -> bool:
        """Returns true if the queue is empty, false otherwise. O(1)."""
        return not self.stack_enqueue

# --- Robust Solution: Amortized O(1) Dequeue/Peek ---
class MyQueueRobustAmortized:
    """
    Implements a queue using two stacks (`in_stack` and `out_stack`).
    Enqueue is O(1). Dequeue and Peek are O(1) amortized.
    Elements are moved from in_stack to out_stack only when out_stack is empty.
    """
    def __init__(self):
        self.in_stack = []  # For enqueue operations (elements pushed here)
        self.out_stack = [] # For dequeue and peek operations (elements popped from here)

    def enqueue(self, x: int) -> None:
        """Pushes element x to the back of the queue. O(1)."""
        self.in_stack.append(x)

    def _transfer_if_needed(self) -> None:
        """
        Helper function: If out_stack is empty, transfer elements from in_stack.
        This operation is O(N) when it happens (where N is size of in_stack),
        but its cost is amortized over many dequeue/peek operations.
        When transferring, elements from in_stack are popped and appended to out_stack,
        reversing their order, so the oldest element from in_stack becomes top of out_stack.
        """
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def dequeue(self) -> int:
        """
        Removes the element from the front of the queue and returns it. Amortized O(1).
        """
        if self.empty(): # Checks both stacks
            raise IndexError("dequeue from empty queue")
        self._transfer_if_needed() # Ensure out_stack has the front element if available
        return self.out_stack.pop()

    def peek(self) -> int:
        """
        Returns the element at the front of the queue. Amortized O(1).
        """
        if self.empty(): # Checks both stacks
            raise IndexError("peek from empty queue")
        self._transfer_if_needed() # Ensure out_stack has the front element if available
        return self.out_stack[-1] # Peek at the top of out_stack

    def empty(self) -> bool:
        """Returns true if the queue is empty, false otherwise. O(1)."""
        return not self.in_stack and not self.out_stack

# --- Jedi Solution: Analysis and Python's `collections.deque` ---
# **Complexity Analysis:**
# 1. Simple Solution (MyQueueSimple):
#    - `enqueue(x)`: O(1) - Appending to a list (stack).
#    - `dequeue()`: O(N) - Involves two full transfers of N elements in the worst case.
#    - `peek()`: O(N) - Similar to dequeue, involves transfers to find the front.
#    - `empty()`: O(1).
#    - This approach is inefficient if dequeue/peek operations are frequent.

# 2. Robust Solution (MyQueueRobustAmortized):
#    - `enqueue(x)`: O(1) - Appending to `in_stack`.
#    - `dequeue()`: Amortized O(1).
#        - Worst-case for a single operation: O(N) if `out_stack` is empty and `in_stack` has N elements that need transferring.
#        - However, each element is moved from `in_stack` to `out_stack` at most once and popped from `out_stack` once.
#          Over a sequence of M operations (where M >= N), the total time for all transfers and pops is proportional to M.
#          So, the average cost per operation is O(1).
#    - `peek()`: Amortized O(1) - Same reasoning as `dequeue`.
#    - `empty()`: O(1).
#    - This is generally the preferred two-stack queue implementation due to better amortized costs.

# **Amortized Analysis Briefly Explained:**
# Amortized analysis considers the average cost of an operation over a sequence of operations.
# Even if one operation in the sequence is expensive (like the transfer in `_transfer_if_needed`),
# its cost can be "spread out" or "amortized" over other less expensive operations,
# leading to a good average cost per operation.

# **Python's Standard Solution: `collections.deque`**
# For most practical purposes in Python, if you need a queue (FIFO), you should use `collections.deque`.
# `deque` (double-ended queue) is implemented in C and is highly optimized. It provides
# O(1) time complexity for append (enqueue at the right end) and popleft (dequeue from the left end) operations.

# Example using `collections.deque`:
#   from collections import deque # Already imported at the top for this file's example
#   my_python_queue = deque()
#   my_python_queue.append(1)    # Enqueue (add to right)
#   my_python_queue.append(2)
#   print(my_python_queue.popleft()) # Dequeue (remove from left): prints 1
#   if my_python_queue: # Check if not empty
#       print(my_python_queue[0])    # Peek at front (leftmost element): prints 2
#   print(not my_python_queue)       # Empty check (False if not empty)

# --- Example Usage ---
if __name__ == "__main__":
    print("--- MyQueueSimple (Dequeue Costly) ---")
    q_simple = MyQueueSimple()
    q_simple.enqueue(1)
    q_simple.enqueue(2)
    print(f"Peek: {q_simple.peek()}")  # Expected: 1
    print(f"Dequeue: {q_simple.dequeue()}")  # Expected: 1
    q_simple.enqueue(3) # Queue: [2, 3]
    print(f"Peek: {q_simple.peek()}") # Expected: 2
    print(f"Dequeue: {q_simple.dequeue()}")  # Expected: 2
    print(f"Dequeue: {q_simple.dequeue()}")  # Expected: 3
    print(f"Is empty: {q_simple.empty()}") # Expected: True
    try:
        print(f"Peek from empty: {q_simple.peek()}")
    except IndexError as e:
        print(f"Error: {e}")
    try:
        print(f"Dequeue from empty: {q_simple.dequeue()}")
    except IndexError as e:
        print(f"Error: {e}")


    print("\n--- MyQueueRobustAmortized (Amortized O(1) Dequeue/Peek) ---")
    q_robust = MyQueueRobustAmortized()
    q_robust.enqueue(10)
    q_robust.enqueue(20) # in_stack: [10, 20], out_stack: []
    print(f"Peek: {q_robust.peek()}")  # Expected: 10 (triggers transfer: in_stack:[], out_stack:[20,10])
    print(f"Dequeue: {q_robust.dequeue()}")  # Expected: 10 (out_stack: [20])
    q_robust.enqueue(30) # in_stack: [30], out_stack: [20]
    print(f"Peek: {q_robust.peek()}") # Expected: 20 (from out_stack)
    print(f"Dequeue: {q_robust.dequeue()}")  # Expected: 20 (out_stack is now empty)
    # Now out_stack is empty, in_stack has [30]. Next peek/dequeue triggers transfer.
    print(f"Peek: {q_robust.peek()}") # Expected: 30 (triggers transfer: in_stack:[], out_stack:[30])
    print(f"Dequeue: {q_robust.dequeue()}")  # Expected: 30 (out_stack is empty)
    print(f"Is empty: {q_robust.empty()}") # Expected: True
    try:
        print(f"Peek from empty: {q_robust.peek()}")
    except IndexError as e:
        print(f"Error: {e}")
    try:
        print(f"Dequeue from empty: {q_robust.dequeue()}")
    except IndexError as e:
        print(f"Error: {e}")

    print("\n--- Jedi Solution Discussion (collections.deque) ---")
    print("See comments in the Jedi Solution section for analysis and `collections.deque` info.")
    # from collections import deque # Already imported at the top
    my_python_queue = deque()
    my_python_queue.append(100) # Enqueue
    my_python_queue.append(200) # Enqueue
    if my_python_queue: # Check if not empty
      print(f"collections.deque example: peek (my_python_queue[0]): {my_python_queue[0]}") # Expected: 100
    print(f"collections.deque example: dequeue (popleft()): {my_python_queue.popleft()}") # Expected: 100
    if not my_python_queue: # Check if empty
        print("collections.deque is empty after one pop.")
    else:
        print(f"collections.deque example: is empty (not my_python_queue): {not my_python_queue}") # Expected: False
        print(f"collections.deque example: peek (my_python_queue[0]): {my_python_queue[0]}") # Expected: 200
    my_python_queue.popleft() # Dequeue 200
    print(f"collections.deque example: is empty after two pops (not my_python_queue): {not my_python_queue}") # Expected: True