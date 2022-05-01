# Python implements List as dynamic arrays
# we can store different types of items in an array/list
# random access feature: accessing data in O(1)
# complex data structure use arrays because of random indexing - o(1)
# stacks, queues, dictionaries (hash-tables)
# matrix-related operations

# small arrays: not wasting too much memory but resize array in O(n) frequently
# large arrays: waste memory but no resize operation

# careful about using built-in lists in Python: they are slow because they are not contiguous in memory
# instead, you should consider using NumPy library, that contains a list in a way the the items are stored in contiguous position in memory

array = [1, 'hi', 3.4, 3, 123]
print(array)

# random indexing
print(array[1])
print(array[:]) # entire array
print(array[0:2]) #first 2 items
print(array[1:3]) #index 1 until 3
print(array[:-1]) # all items exception last one

array[1] = 'hello'
print(array[:])

# linear search
array2 = [1,2,3,4]
max = array2[0]

for num in array2:
  if num > max:
    max = num
print (max)

# add in the begginning of array
array2.insert(0, 'added')
print(array2[:])

# add in the middle of array
print(array2.insert(len(array2) // 2, 'added in the middle') )
print(array2[:])

# add in the end of an array
array2.append('end')
print(array2)

# removing from array
array2.remove('added in the middle') # first occurrence
print(array2[:])

# changing value of an existing array
array2[2] = 'value was changed'
print(array2)