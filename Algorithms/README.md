# Algorithms

This section provides explanations and examples for various algorithms commonly encountered in software development and technical interviews. Each algorithm is presented with:

1.  A **Simple Solution**: Illustrates the core concept.
2.  A **More Robust Solution**: Handles edge cases and may offer better performance or clarity.
3.  A **Jedi's Approach**: An advanced, optimized, or particularly insightful solution.

We aim to solve problems using core language features, minimizing reliance on third-party libraries, but will mention them where their use is common or offers significant advantages.

## Table of Contents

*   [Binary Search](#binary-search)
*   [Selection Sort](#selection-sort)
*   [Quick Sort](#quick-sort)
*   [Depth First Search (DFS)](#depth-first-search-dfs)
*   [Breadth First Search (BFS)](#breadth-first-search-bfs)
*   *(More algorithm links will be added to this TOC)*

---

## Binary Search

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

[Link to implementation](./1-BinarySearch/1-BinarySearch.py)

### 1. Simple Solution (Iterative)

The simple solution provides a straightforward iterative implementation.
- It uses two pointers, `low` and `high`, to define the current search space.
- In each step, it calculates the middle index and compares the element at this index with the target item.
- The search space is halved based on this comparison.
- This approach is easy to understand and implement.

### 2. Robust Solution (Recursive)

The robust solution offers a recursive implementation.
- It breaks the problem down into smaller subproblems.
- The base cases for the recursion are when the item is found or the search space is empty.
- This version can be more intuitive for those familiar with recursion and clearly shows the divide-and-conquer nature of the algorithm.
- Considerations for handling duplicates (e.g., finding the first or last occurrence) can be incorporated.

### 3. Jedi Solution (Using `bisect` module)

The Jedi solution leverages Python's built-in `bisect` module, specifically `bisect_left`.
- The `bisect` module provides highly optimized functions for working with sorted lists.
- `bisect_left` returns an insertion point which helps in finding the item or determining where it would be inserted to maintain sort order.
- This approach is very concise and typically more performant than a manually implemented version due to its C implementation details.
- It's a Pythonic way to handle searching in sorted sequences.

---

## Selection Sort

Selection Sort is a simple in-place comparison sorting algorithm. It divides the input list into two parts: a sorted sublist of items which is built up from left to right at the front (left) of the list and a sublist of the remaining unsorted items that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, swapping it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.

[Link to implementation](./2-SelectionSort/2-SelectionSort.py)

### 1. Simple Solution (In-Place)

The simple solution provides a standard, in-place implementation of Selection Sort.
- It iterates through the list, and for each element, it finds the minimum element in the remaining unsorted portion of the list.
- This minimum element is then swapped with the element at the current position.
- This approach sorts the list directly, using O(1) auxiliary space.

### 2. Robust Solution (Out-of-Place, Conceptual)

The robust solution demonstrates an out-of-place version of Selection Sort.
- It explicitly creates a copy of the input array to preserve the original.
- It iteratively finds the smallest element in its working copy, appends it to a new list, and removes it from the working copy.
- While conceptually illustrating Selection Sort, this specific implementation is less efficient for large lists due to the repeated use of `list.pop()` from potentially the middle of the list (an O(N) operation within a loop). It requires O(N) space for the new list and the copy.

### 3. Jedi Solution (In-Depth Analysis)

The Jedi solution focuses on a deeper understanding of the in-place Selection Sort:
- **Time Complexity**: Strictly O(N^2) for comparisons in all cases (best, average, worst) because the loops always iterate through the entire unsorted portion. Number of swaps is O(N).
- **Space Complexity**: O(1) auxiliary space, as it sorts the data in-place.
- **Stability**: The typical implementation (like our simple one) is **not stable**. Equal elements might not maintain their original relative order after sorting. It can be made stable with modifications (e.g., if instead of swapping, elements are inserted and following elements are shifted).
- **Use Cases**: Best suited for small lists or when the number of swaps is a critical performance factor (as it performs at most N-1 swaps).
- **Comparison**: It's generally outperformed by Insertion Sort for small lists and by more advanced algorithms like Merge Sort or Quick Sort for larger lists. Compared to Bubble Sort, it usually performs fewer swaps.

---

## Quick Sort

Quick Sort is a highly efficient, divide-and-conquer sorting algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

[Link to implementation](./3-QuickSort.py/1-QuickSort.py)

### 1. Simple Solution (Out-of-Place)

The simple solution illustrates Quick Sort using a straightforward, out-of-place approach.
- It typically selects the first element as the pivot.
- It uses list comprehensions or similar methods to create new lists for elements smaller than the pivot and elements greater than the pivot.
- While easy to understand, this version is not memory-efficient for large datasets due to the creation of new lists at each recursion step (O(N) auxiliary space, not including recursion stack).

### 2. Robust Solution (In-Place with Lomuto Partition)

The robust solution provides an in-place implementation of Quick Sort using the Lomuto partition scheme.
- **Lomuto Partition Scheme**: Typically uses the last element of the current segment as the pivot. It iterates through the segment, moving elements smaller than or equal to the pivot to one side. The pivot is then swapped into its final sorted position.
- **In-Place Sorting**: Modifies the array directly, using O(log N) auxiliary space on average for the recursion call stack.
- This version is more memory-efficient than the simple out-of-place one.

### 3. Jedi Solution (In-Place with Hoare Partition and In-Depth Analysis)

The Jedi solution explores a more optimized in-place version using the Hoare partition scheme and provides deeper insights:
- **Hoare Partition Scheme**: Typically uses the first element as the pivot (or a chosen one). It uses two pointers that scan towards each other from opposite ends of the segment, swapping elements that are on the wrong side of the pivot. It's generally more efficient than Lomuto (fewer swaps on average). The pivot element itself doesn't necessarily end up in its final sorted position after one pass, but the partition is effective for recursion.
- **Analysis & Optimizations**:
    - **Pivot Selection**: Discusses strategies like median-of-three or randomized pivot selection to improve performance and avoid worst-case O(N^2) complexity (which occurs with already sorted/reverse sorted data if naive pivot selection is used).
    - **Time Complexity**: Average case is O(N log N), worst case is O(N^2).
    - **Space Complexity**: For in-place versions, O(log N) on average for the recursion stack, O(N) in the worst case.
    - **Stability**: Quick Sort is not a stable sorting algorithm.
    - **Further Optimizations**: Mentions concepts like tail call optimization (though not directly optimized by Python's default interpreter) and using Insertion Sort for small sub-arrays (hybrid approach) to improve performance.

---

## Depth First Search (DFS)

Depth First Search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (or an arbitrary node in a graph) and explores as far as possible along each branch before backtracking.

[Link to implementation](./4-DFS/4-DFS.py)

### 1. Simple Solution (Recursive)

The simple solution provides a basic recursive implementation of DFS.
- It typically uses a `visited` set to keep track of nodes already explored.
- For a given node, it marks it as visited and then recursively calls DFS for each of its unvisited neighbors.
- This approach is intuitive and closely mirrors the definition of DFS but can lead to `RecursionError` for very deep graphs. It explores only the connected component reachable from the start node.

### 2. Robust Solution (Iterative, Handles Disconnected Graphs)

The robust solution offers an iterative DFS using an explicit stack, with added capabilities:
- **Handles Disconnected Graphs**: It iterates through all nodes in the graph, starting a DFS traversal if a node hasn't been visited yet. This ensures all connected components are explored.
- **Explicit Stack**: Manages the traversal path using a stack, avoiding recursion depth limits.
- **Cycle Detection Aid**: The structure can be easily extended to detect cycles by keeping track of nodes currently in the 'recursion path' (i.e., in the explicit stack or a secondary set tracking the current path). If a neighbor is encountered that is already in the current path, a cycle is detected.

### 3. Jedi Solution (Iterative with Discovery/Finish Times & Applications)

The Jedi solution provides an advanced iterative DFS that also calculates discovery and finish times for each node.
- **Discovery and Finish Times**:
    - *Discovery Time*: The 'time' (step) at which a node is first visited.
    - *Finish Time*: The 'time' (step) at which the algorithm is done processing a node and all its descendants.
- **Handles Disconnected Graphs**: Similar to the robust version, it processes all components.
- **Applications**: These times are crucial for various advanced graph algorithms:
    - **Topological Sorting (for Directed Acyclic Graphs - DAGs)**: Sorting nodes such that for every directed edge from node `u` to node `v`, node `u` comes before node `v` in the ordering. A linear ordering of vertices of a DAG can be obtained by sorting them in decreasing order of their finish times.
    - **Finding Strongly Connected Components (in Directed Graphs)**: Using algorithms like Tarjan's or Kosaraju's, which are based on DFS and its properties (like finish times).
    - **Cycle Detection**: Cycles can be identified using back edges, which are edges connecting a node to an ancestor in the DFS tree (identifiable using discovery/finish times or path stack).

---

## Breadth First Search (BFS)

Breadth First Search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at an arbitrary node of a graph and explores the neighbor nodes first (i.e., all nodes at the present "depth" or "level") before moving on to the nodes at the next depth level. It typically uses a queue to keep track of the next location to visit.

[Link to implementation](./5-BFS/5-BFS.py)

### 1. Simple Solution (Iterative with Queue)

The simple solution provides a standard iterative implementation of BFS using a queue (`collections.deque` in Python).
- It starts by enqueuing the source node and marking it as visited.
- In a loop, it dequeues a node, processes it (e.g., adds to path), and then enqueues all its unvisited neighbors, marking them as visited.
- This approach explores the graph layer by layer and finds the shortest path in terms of the number of edges from the source node to all other nodes in its connected component.

### 2. Robust Solution (Handles Disconnected Graphs, Path Reconstruction)

The robust solution extends the simple BFS to handle disconnected graphs and explicitly reconstructs paths:
- **Handles Disconnected Graphs**: It iterates through all nodes in the graph, starting a BFS traversal if a node hasn't been visited yet, ensuring all connected components are explored.
- **Path and Distance Tracking**: For each component explored, it not only performs the traversal but also keeps track of the shortest path (list of nodes) and distance (number of edges) from the component's starting node to every other node within that component.

### 3. Jedi Solution (Bidirectional BFS & Applications)

The Jedi solution focuses on a specialized and often more efficient variant for a specific problem, plus a broader look at applications:
- **Bidirectional BFS**: This technique is primarily used for finding the shortest path between two specific nodes (source and target). It runs two simultaneous BFS traversals—one starting from the source and moving forward, and another starting from the target and moving backward. The search stops when the two traversals meet. This can significantly reduce the search space and time compared to a unidirectional BFS, especially in large graphs.
- **Applications of BFS**:
    - **Shortest Path in Unweighted Graphs**: BFS is guaranteed to find the shortest path (in terms of number of edges) between a start node and all other reachable nodes.
    - **Connected Components**: Can be used to find all connected components in a graph.
    - **Level Order Traversal**: For trees (which are special types of graphs), BFS gives a level-order traversal.
    - **Network Analysis**: Used in algorithms like finding the shortest route in peer-to-peer networks, web crawlers, etc.
    - **Testing Bipartiteness**: A graph is bipartite if it can be colored with two colors such that no two adjacent nodes have the same color. BFS can be used to test this.

---
*(More algorithm sections will be added here)*
