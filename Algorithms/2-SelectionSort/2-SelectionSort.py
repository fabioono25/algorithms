# here is an implementation of Selection sort

#Time complexity: O(n^2), Space complexity: O(n)
def selection_sort_basic(arr):
  temp = []
  length = len(arr)
  
  for i in range(length):
    for j in range(i + 1, length):
      if (arr[i] > arr[j]):
        arr[j], arr[i] = arr[i], arr[j]
  return arr

def selection_sort(arr):
  new_arr = []
  for i in range(len(arr)):
    smallest = find_smallest(arr)
    new_arr.append(arr.pop(smallest))
  return new_arr

def find_smallest(arr):
  smallest = arr[0] # stores the smallest value
  smallest_index = 0 # stores the index of the smallest value
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index

print(selection_sort_basic([5, 3, 6, 2, 10])) # => [2, 3, 5, 6, 10]
print(selection_sort_basic([5, 11, 6, 2, 10])) # => [2, 5, 6, 10, 11]

print(selection_sort([5, 3, 6, 2, 10])) # => [2, 3, 5, 6, 10]
print(selection_sort([5, 11, 6, 2, 10])) # => [2, 5, 6, 10, 11]