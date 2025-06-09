# Data Structures/3-Stack/1-StackUsingQueue.py
# Problem: Implement a last-in-first-out (LIFO) stack using only queues.
# The implemented stack should support push, top, pop, and empty operations.
# Constraint: Use only standard queue operations (enqueue, dequeue, peek, size, is_empty).

from collections import deque

# --- Simple Solution: Push O(N), Pop/Top O(1) (using one primary queue) ---
class MyStackSimple:
    """
    Implements a stack using one primary queue.
    - push(x): To push an element, enqueue it, then rotate the queue so the new
               element becomes the front. This makes push O(N).
    - pop(): Dequeue from the front. O(1).
    - top(): Peek at the front. O(1).
    """
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        """Pushes element x to the top of the stack. O(N)."""
        self.q.append(x) # Enqueue new element
        # Rotate the queue to move the new element to the front
        # This ensures the last pushed element is at the front of the queue (like top of stack)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """Removes the element on the top of the stack and returns it. O(1)."""
        if self.empty():
            raise IndexError("pop from empty stack")
        return self.q.popleft() # Front of queue is top of stack

    def top(self) -> int:
        """Returns the element on the top of the stack. O(1)."""
        if self.empty():
            raise IndexError("top from empty stack")
        return self.q[0] # Peek front element of queue (top of stack)

    def empty(self) -> bool:
        """Returns true if the stack is empty, false otherwise. O(1)."""
        return not self.q

# --- Robust Solution: Push O(1), Pop/Top O(N) (using two queues) ---
class MyStackRobust:
    """
    Implements a stack using two queues, q1 (primary) and q2 (helper).
    - push(x): Enqueue to q1. O(1).
    - pop(): Transfer N-1 elements from q1 to q2, dequeue the Nth (last) from q1.
             Then swap roles of q1 and q2 so q1 is ready for next push. O(N).
    - top(): Similar to pop, but re-enqueue the top element back to q1 after peeking. O(N).
    """
    def __init__(self):
        self.q1 = deque() # Primary queue for pushes and holding elements
        self.q2 = deque() # Helper queue for pop/top operations

    def push(self, x: int) -> None:
        """Pushes element x to the top of the stack. O(1)."""
        self.q1.append(x) # New elements are always added to q1

    def pop(self) -> int:
        """Removes the element on the top of the stack and returns it. O(N)."""
        if self.empty():
            raise IndexError("pop from empty stack")

        # Move all but the last element from q1 to q2
        # The last element remaining in q1 is the "top" of the stack.
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        # Dequeue the top element (which is the last one enqueued into q1)
        top_element = self.q1.popleft()

        # q2 now holds all other elements in their correct relative order.
        # Swap q1 and q2 so that q1 becomes the main queue again (or q2 becomes empty for next op).
        self.q1, self.q2 = self.q2, self.q1 # q2 is now empty, q1 has the elements

        return top_element

    def top(self) -> int:
        """Returns the element on the top of the stack. O(N)."""
        if self.empty():
            raise IndexError("top from empty stack")

        # Move all but the last element from q1 to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        # The last element in q1 is the top element
        top_element = self.q1[0]

        # Move this last element to q2 as well, so all elements are now in q2
        self.q2.append(self.q1.popleft())

        # Swap q1 and q2 to restore state
        self.q1, self.q2 = self.q2, self.q1
        return top_element

    def empty(self) -> bool:
        """Returns true if the stack is empty, false otherwise. O(1)."""
        # The active elements are always in q1 (after potential swap in pop/top)
        return not self.q1


# --- Jedi Solution: Analysis and Python's List as a Stack ---
# **Complexity Analysis:**
# 1. MyStackSimple (Push O(N), Pop/Top O(1)):
#    - `push(x)`: O(N) due to rotation of N elements in the queue. Each `append` is O(1),
#      each `popleft` is O(1). N-1 rotations are done.
#    - `pop()`: O(1) as it's a `popleft()` from the deque.
#    - `top()`: O(1) as it's accessing the first element (`q[0]`).
#    - `empty()`: O(1).
#    - This approach is efficient if pop/top operations are far more frequent than pushes.

# 2. MyStackRobust (Push O(1), Pop/Top O(N)):
#    - `push(x)`: O(1) as it's an `append()` to `q1`.
#    - `pop()`: O(N) because N-1 elements are moved from `q1` to `q2` (N-1 `popleft`
#      and N-1 `append` operations, each O(1)).
#    - `top()`: O(N) for similar reasons to `pop()`.
#    - `empty()`: O(1).
#    - This approach is efficient if pushes are far more frequent than pop/top operations.

# **Which to choose?**
# The choice between `MyStackSimple` and `MyStackRobust` depends on the expected frequency
# of push vs. pop/top operations. Neither is ideal for all scenarios due to the O(N)
# operation in one of their core functions if striving for overall stack-like efficiency.
# True stack operations are typically all O(1) (amortized for list-based Python stacks).

# **Python's Built-in List as a Stack:**
# In Python, lists can be used directly as stacks with efficient amortized O(1) operations:
#   - `append()` for push (amortized O(1)).
#   - `pop()` (from the end) for pop (O(1)).
#   - Accessing the last element (`my_list[-1]`) for top (O(1)).
# This is typically the most Pythonic and performant way to implement a stack if
# the constraint of using only queues is not present.

# Example using a list as a stack:
#   py_stack = []
#   py_stack.append(1)  # push
#   py_stack.append(2)
#   print(py_stack[-1]) # top: prints 2
#   print(py_stack.pop()) # pop: prints 2
#   print(not py_stack) # empty: prints False (if not empty)

# --- Example Usage ---
if __name__ == "__main__":
    print("--- MyStackSimple (Push O(N), Pop O(1)) ---")
    s_simple = MyStackSimple()
    s_simple.push(1) # q: [1]
    s_simple.push(2) # q: rotate [1,2] -> [2,1]
    print(f"Top: {s_simple.top()}")    # Expected: 2
    print(f"Pop: {s_simple.pop()}")    # Expected: 2, q is now [1]
    s_simple.push(3) # q: rotate [1,3] -> [3,1]
    print(f"Top: {s_simple.top()}")    # Expected: 3
    print(f"Pop: {s_simple.pop()}")    # Expected: 3, q is now [1]
    print(f"Pop: {s_simple.pop()}")    # Expected: 1
    print(f"Is empty: {s_simple.empty()}") # Expected: True
    try:
        print(s_simple.top())
    except IndexError as e:
        print(f"Error on top from empty (Simple): {e}")

    print("\n--- MyStackRobust (Push O(1), Pop O(N)) ---")
    s_robust = MyStackRobust()
    s_robust.push(10) # q1: [10]
    s_robust.push(20) # q1: [10, 20]
    print(f"Top: {s_robust.top()}")    # Expected: 20. After top, q1 is [10, 20]
    print(f"Pop: {s_robust.pop()}")    # Expected: 20. After pop, q1 is [10]
    s_robust.push(30) # q1: [10, 30]
    print(f"Top: {s_robust.top()}")    # Expected: 30
    print(f"Pop: {s_robust.pop()}")    # Expected: 30
    print(f"Pop: {s_robust.pop()}")    # Expected: 10
    print(f"Is empty: {s_robust.empty()}") # Expected: True
    try:
        s_robust.pop()
    except IndexError as e:
        print(f"Error on pop from empty (Robust): {e}")

    print("\n--- Jedi Solution Discussion (Python List as Stack) ---")
    print("See comments in the Jedi Solution section for analysis.")
    py_stack = []
    py_stack.append(100)
    py_stack.append(200)
    if py_stack: print(f"Python list as stack: Top (py_stack[-1]): {py_stack[-1]}")
    if py_stack: print(f"Python list as stack: Pop (py_stack.pop()): {py_stack.pop()}")
    print(f"Python list as stack: Is empty (not py_stack): {not py_stack}")
    if py_stack: py_stack.pop()
    print(f"Python list as stack: Is empty after all pops (not py_stack): {not py_stack}")
