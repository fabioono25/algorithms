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
*   [HashTable](#hashtable)
*   [LinkedList](#linkedlist)
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
*(More data structure sections will be added here)*
