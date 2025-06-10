# Data Structures

This section provides explanations and examples for various data structures fundamental to computer science and software engineering. The aim is to offer resources for those looking to master these concepts, particularly for technical interviews.

Each data structure or associated problem will be presented with:

1.  A **Simple Solution/Implementation**: Illustrates the core concept or a basic way to use the data structure.
2.  A **More Robust Solution/Implementation**: May handle more edge cases, offer better performance for certain operations, or provide a more complete implementation.
3.  A **Jedi's Approach**: An advanced perspective, perhaps focusing on optimizations, common trade-offs, complex use cases, or a from-scratch implementation if appropriate.

We will focus on implementing and using these data structures with core language features where possible, minimizing reliance on ready-made library versions for foundational understanding, but will mention standard library versions where relevant.

## Table of Contents

*   [Array](#array)
    *   [Reverse an Array](#reverse-an-array)
    *   [Two Sum](#two-sum)
    *   [Median of Two Sorted Arrays](#median-of-two-sorted-arrays)
*   [Queue](#queue)
    *   [Implement a Queue using two Stacks](#implement-a-queue-using-two-stacks)
*   [Stack](#stack)
    *   [Implement a Stack using two Queues](#implement-a-stack-using-two-queues)
    *   [Valid Parentheses](#valid-parentheses)
*   [HashTable](#hashtable)
    *   [Implement a Simple HashTable](#implement-a-simple-hashtable)
    *   [Problem: Two Out Of Three](#problem-two-out-of-three)
*   [LinkedList](#linkedlist)
    *   [Implement a Singly LinkedList](#implement-a-singly-linkedlist)
    *   [Problem: Merge Two Sorted Lists](#problem-merge-two-sorted-lists)
*   *(More data structures will be added here)*

---

## Array

Arrays (or lists in Python) are fundamental data structures used to store collections of elements. Python lists are dynamic and can hold heterogeneous data types.

For a general overview of Python list operations and features, please see the tutorial style explanations in:
[Python List Basics](./1-Array/0-Lists.py)

Below are specific array-based problems with different solution approaches:

### Reverse an Array

**Problem**: Given an array, reverse its elements.

[Link to implementation](./1-Array/1-Reverse.py)

*   **Simple Solution (Slicing `[::-1]`):** Creates a reversed copy of the array. O(N) time, O(N) space. Very Pythonic for out-of-place reversal.
*   **Robust Solution (Two-Pointer In-Place):** Modifies the array directly by swapping elements from both ends. O(N) time, O(1) space. Ideal for memory efficiency or when the original list must be changed.
*   **Jedi Solution (Analysis & Built-ins):** Discusses complexities, Python's `list.reverse()` method (in-place, optimized), reversing immutable sequences (strings, tuples), and handling iterators.

### Two Sum

**Problem**: Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

[Link to implementation](./1-Array/7-TwoSum.py)

*   **Simple Solution (Brute Force):** Uses nested loops to check every pair of numbers. O(N^2) time, O(1) space.
*   **Robust Solution (Hash Table):** Uses a hash table (dictionary) to store numbers and their indices, allowing O(1) average time lookups for complements. O(N) time, O(N) space.
*   **Jedi Solution (Sorted Array & Variations):**
    *   Explores the two-pointer technique for sorted arrays (O(N) time, O(1) space after sorting).
    *   Discusses problem variations: returning numbers instead of indices, handling multiple pairs, and implications of large numbers in other languages.

### Median of Two Sorted Arrays

**Problem**: Given two sorted arrays, `nums1` and `nums2`, find the median of the combined sorted array.

[Link to implementation](./1-Array/10-MedianOfTwoSortedArrays.py)

*   **Simple Solution (Merge and Find):** Merges the two arrays into a single sorted array, then finds the median. O(m+n) time, O(m+n) space.
*   **Robust Solution (Iterative Median Search):** Simulates the merge process iteratively, only keeping track of elements around the median position. O(m+n) time, O(1) space.
*   **Jedi Solution (Binary Search on Partitions):** The optimal solution using binary search on the partitions of the smaller array. Achieves O(log(min(m,n))) time and O(1) space. Involves careful handling of partition boundaries and median calculation for odd/even total lengths.

---

## Queue

A queue is a linear data structure that follows the First-In, First-Out (FIFO) principle. Elements are added at one end (rear/enqueue) and removed from the other end (front/dequeue).

### Implement a Queue using two Stacks

**Problem**: Design a queue using only two stacks as underlying data storage. The queue should support standard operations like enqueue, dequeue, peek, and empty.

[Link to implementation](./2-Queue/1-QueueUsingStack.py)

*   **Simple Solution (Dequeue Costly):**
    *   Uses one stack for enqueue operations (O(1)).
    *   For dequeue or peek, all elements are transferred to a helper stack to reverse their order and access the front element, then transferred back. These operations become O(N).
    *   Easy to conceptualize but inefficient for frequent dequeue/peek.

*   **Robust Solution (Amortized O(1) Dequeue/Peek):**
    *   Uses an `in_stack` for enqueues (O(1)) and an `out_stack` for dequeues/peeks.
    *   Elements are moved from `in_stack` to `out_stack` only when `out_stack` is empty (an O(N) operation).
    *   Subsequent dequeues/peeks from a non-empty `out_stack` are O(1).
    *   This results in an amortized O(1) time complexity for dequeue and peek operations, making it generally more efficient.

*   **Jedi Solution (Analysis & `collections.deque`):**
    *   Provides a comparative analysis of the time complexities of the two-stack approaches.
    *   Explains the concept of amortized analysis in the context of the robust solution.
    *   Highlights Python's `collections.deque` as the standard, highly optimized C-implemented class for efficient O(1) queue operations (append and popleft) and recommends its use for practical applications.

---

## Stack

A stack is a linear data structure that follows the Last-In, First-Out (LIFO) principle. Elements are added (pushed) and removed (popped) from the same end, called the top of the stack.

### Implement a Stack using two Queues

**Problem**: Design a LIFO stack using only two queues as underlying data storage. The stack should support standard operations like push, pop, top, and empty. (Note: Standard queue operations are assumed: enqueue, dequeue, peek, size, is_empty).

[Link to implementation](./3-Stack/1-StackUsingQueue.py)

*   **Simple Solution (Push O(N), Pop/Top O(1)):**
    *   Uses one primary queue. To push, the new element is enqueued, and then the queue is rotated (N-1 elements dequeued and re-enqueued) to bring the new element to the front. Pop/Top operations are then O(1) from the front of the queue.
*   **Robust Solution (Push O(1), Pop/Top O(N)):**
    *   Uses two queues (`q1`, `q2`). Push is O(1) to `q1`. To pop/top, N-1 elements are moved from `q1` to `q2`, the Nth element is processed from `q1`, and then `q1` and `q2` swap roles.
*   **Jedi Solution (Analysis & Python List as Stack):**
    *   Compares complexities of the two approaches, noting that neither is ideal due to an O(N) operation.
    *   Recommends using Python's built-in list (`append`/`pop`) for efficient stack operations if not constrained to use queues.

### Valid Parentheses

**Problem**: Given a string `s` containing just '(', ')', '{', '}', '[' and ']', determine if the input string is valid based on correct bracket opening/closing and order.

[Link to implementation](./3-Stack/2-ValidParenthesis.py)

*   **Simple Solution (Single Parenthesis Type):**
    *   Illustrates basic stack logic using only `(` and `)`. Pushes `(` on stack, pops on `)`. Valid if stack is empty at the end.
*   **Robust Solution (Multiple Parenthesis Types):**
    *   Handles `()`, `[]`, and `{}`. Pushes opening brackets onto a stack. When a closing bracket is encountered, checks if the stack is non-empty and its top matches the corresponding opening bracket.
*   **Jedi Solution (Mapping & Edge Cases):**
    *   Uses a dictionary to map closing brackets to opening ones for cleaner logic.
    *   Provides detailed discussion of edge cases (empty string, only open/close brackets, mismatches) and efficiency (O(N) time, O(N) space). Notes application in parsing.

---

## HashTable

A HashTable is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.

### Implement a Simple HashTable

**Concept**: Building a HashTable from scratch to understand its core mechanics, including hash function design, collision resolution, and dynamic resizing.

[Link to implementation](./4-HashTable/0-SimpleHashTable.py)

*   **Simple Solution (Basic Chaining):**
    *   Uses a basic modulo hash function (`abs(hash(key)) % size`).
    *   Collisions are handled by chaining, where each bucket is a list of (key, value) pairs.
    *   Implements `put`, `get`, and `remove` operations.
*   **Robust Solution (Chaining with Resizing):**
    *   Extends the simple version by adding dynamic resizing.
    *   Tracks the number of elements and a load factor.
    *   When the load factor exceeds a threshold (e.g., 0.75), the table size is increased (e.g., doubled), and all existing elements are rehashed into the new table.
*   **Jedi Solution (Discussion of Advanced Concepts):**
    *   Discusses critical aspects:
        *   **Hash Functions**: Properties of good hash functions, issues with basic ones, use of prime numbers for table sizes, `__hash__` in custom objects.
        *   **Collision Resolution**: Deeper dive into Chaining vs. Open Addressing (Linear Probing, Quadratic Probing, Double Hashing).
        *   **Load Factor & Resizing**: Importance and amortized cost.
        *   **Python's `dict`/`set`**: Acknowledges Python's highly optimized built-in implementations.

### Problem: Two Out Of Three

**Problem**: Given three integer arrays `nums1`, `nums2`, and `nums3`, return a distinct array containing all values present in at least two of the three arrays.

[Link to implementation](./4-HashTable/1-TwoOutOfThree.py)

*   **Simple Solution (Iterative Checking with Sets & List):**
    *   Converts input lists to sets, finds all unique numbers, then iterates and counts occurrences in each set, adding to a result list if count >= 2. Conceptually simple but can be less optimized than direct set math.
*   **Robust Solution (HashMap for Counting):**
    *   Uses a hash map (dictionary) to count occurrences of each number across the unique elements of the three input arrays (after converting them to sets). Efficient for tallying.
*   **Jedi Solution (Leveraging Sets & `collections.Counter`):**
    *   **Set Operations**: Provides a concise solution using set intersections (`&`) and unions (`|`): `(s1&s2) | (s1&s3) | (s2&s3)`.
    *   **`collections.Counter`**: An alternative using `Counter` to tally occurrences of numbers after converting inputs to sets. Filters for counts >= 2. Both are Pythonic and efficient.

---

## LinkedList

A LinkedList is a linear data structure where elements are not stored at contiguous memory locations; instead, the elements are linked using pointers. Each element (node) typically consists of data and a pointer to the next node in the sequence.

### Implement a Singly LinkedList

**Concept**: Building a Singly Linked List from scratch to understand its fundamental operations and memory management. In a singly linked list, each node points only to the next node in the list.

[Link to implementation](./5-LinkedList/0-SimpleLinkedList.py)

*   **Simple Solution (Basic Operations):**
    *   Includes a `Node` class (data, next pointer).
    *   `SimpleLinkedList` class with `head` pointer.
    *   Implements `append` (O(N) without tail), `prepend` (O(1)), and `display`.
*   **Robust Solution (More Operations & Tail Pointer):**
    *   Extends simple version by adding a `tail` pointer for O(1) `append`.
    *   Tracks `num_elements` for O(1) `get_size`.
    *   Implements `delete` (by key), `search`, and `insert_after_node_data`, with careful handling of head/tail updates.
*   **Jedi Solution (Discussion of Advanced Concepts):**
    *   Analyzes complexities of the robust operations.
    *   Discusses the utility of a **Dummy Head Node** (Sentinel Node) for simplifying edge cases in list manipulations.
    *   Briefly introduces concepts of **Doubly Linked Lists** (with `prev` pointers) and **Circular Linked Lists**.
    *   Compares with Python's built-in `list` and `collections.deque`.

### Problem: Merge Two Sorted Lists

**Problem**: Given the heads of two sorted linked lists, merge them into a single, sorted linked list by splicing together their nodes.

[Link to implementation](./5-LinkedList/1-MergeTwoSortedLists.py)

*   **Simple Solution (Recursive):**
    *   Merges the lists using a recursive approach. Base cases handle empty lists. Recursively determines the next node by comparing current node values from both lists.
    *   Time: O(N+M), Space: O(N+M) for recursion stack.
*   **Robust Solution (Iterative with Dummy Head):**
    *   Merges lists iteratively. Uses a dummy head node to simplify list construction and a `current_tail` pointer to build the new list.
    *   Time: O(N+M), Space: O(1).
*   **Jedi Solution (Analysis & Considerations):**
    *   Compares time/space complexity of recursive vs. iterative solutions.
    *   Emphasizes the utility of the dummy head node technique.
    *   Clarifies that the solutions rearrange existing nodes (in-place splicing).
    *   Mentions the "Merge k Sorted Lists" problem as a common follow-up.

---
*(More data structure sections will be added here)*
