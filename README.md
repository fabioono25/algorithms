# Algoritms

## Arrays:

Characteristics:

- Every item is identified by an index, located in the RAM and next to each other.

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


## Linked Lists:

