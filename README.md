# Data Structures:



## Arrays:

Characteristics:

- They represent an ordered group of elements.

- Every item is identified by an index, located in the RAM and next to each other.

- They are immutable in their essence (arrays, lists in Python).

- They are known as a random access structure, meaning that each element can be accessed directly and in constant time.

- Static arrays have the memory allocation defined at compile time and the memory is allocated in the stack. Fixed size.

- Dynamic arrays is completed at runtime and the memory is allocated in the heap. The size of the array is not fixed.
 
- Some important data structures, like stacks, queues, dictionaries (hashtables) use arrays in their construction, because of the random indexing characteristics.

- When an array becomes "full", it is necessary allocate a larger chunk of memory in the RAM (2x the size of actual array), copying all existing items to this new array [O(n) operation].

- Arrays are easy to understand and implement.

- Fast structures for last items and known indexes.

- Arrays are considered static structures (that must know the size upfront or it must be resized each time).

<p>&nbsp;</p>


<center>

|Operation                          | Time Complexity                         |
|-------------------------------|-----------------------------|
|Access            				  |O(1)	     |
|Search            				  |O(n)	     |
|Insertion        				  |O(n)	     |
|Deletion         				  |O(n)	     |
|Append            				  |O(1)	     |

</center>

## Lists: A versatile, ordered collection that can store various data types.

## Linked Lists: A linear data structure where each element points to the next one.

## Stacks: Follows the Last-In-First-Out (LIFO) principle for element access.

## Queues: Follows the First-In-First-Out (FIFO) principle for element access.

==================================================================================================

# Algorithms:



## Binay Search:

Characteristics:

  - Binary Search is a search algorithm used to find the position of a target value within a **sorted array**.

  - It works by repeatedly dividing the search range **in half** until the target value is found or the search range is empty.

  - Binary Search is **efficient for large datasets** because it eliminates half of the remaining elements in each step.

  - It is most effective on sorted arrays, as **the sorted nature of the array is crucial** to the algorithm's efficiency.

  - Binary Search can be implemented both iteratively and recursively.

  - The algorithm compares the target value with the middle element of the current search range and eliminates one half of the range in each step.

  - If the middle element is not the target, the search range is narrowed down to either the left or the right half, depending on whether the target value is smaller or larger than the middle element.

  - The process continues until the target value is found or the search range is empty.

<p>&nbsp;</p>


<center>

|Operation                          | Time Complexity                         |
|-------------------------------|-----------------------------|
|Access            				  |O(log n)	     |

</center>

Binary Search has a time complexity of O(log n) because in each step, the search range is divided in half, reducing the remaining elements to search exponentially. This makes Binary Search much more efficient than linear search for large datasets. However, it's important to note that Binary Search can only be used on sorted arrays.

Some real-world use cases for binary search:

- Searching in Databases: Binary search is frequently used in databases to locate specific entries based on indexed values. This helps optimize database queries, making searches faster and more efficient.

- Dictionary Lookup: In spell checkers, autocomplete features, or language dictionaries, binary search can be used to quickly find words or phrases, as these are often organized alphabetically or in some order.

- Guessing Games: In games like "20 Questions" or other similar guessing games, binary search can efficiently narrow down possibilities by asking questions that split the search space in half each time.

- File Searching: When searching for a specific term or keyword in a large sorted text file or log file, binary search can be used to quickly find instances of that term.

- Stock Price Lookup: In financial applications, binary search can help locate stock prices within a sorted historical data set, making it easier to analyze trends and historical performance.

- Library Catalogs: In library systems, binary search can be used to find books or resources by title, author, or other attributes.

- Geographical Location Searching: In geographical databases, binary search can assist in locating points of interest, addresses, or geographic coordinates.

- Searching in Arrays or Lists: Whenever you have a sorted list or array of data and you need to find a specific element, binary search can provide a faster alternative to linear search.

- Finding Insertion Points: Binary search can be used to efficiently find the correct position for inserting a new element in a sorted array, helping maintain the sorted order.

- Searching in Game Development: In game development, binary search can be used for collision detection algorithms, ray tracing, and other spatial searching tasks.

- Network Routing: In networking and routing protocols, binary search can assist in identifying optimal routes or nodes in network topologies.

