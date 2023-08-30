# here is an implementation of Quicksort

def quicksort(array):
  if len(array) < 2:
    return array
  
  pivot = array[0]
  less = [i for i in array[1:] if i <= pivot]
  greater = [i for i in array[1:] if i > pivot]

  return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([5, 3, 6, 2, 10])) # => [2, 3, 5, 6, 10]
print(quicksort([5, 11, 6, 2, 10])) # => [2, 5, 6, 10, 11]
