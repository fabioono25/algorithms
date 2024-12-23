# Find the minimum and maximum element in an array

# Time complexity: O(n) - Space complexity: O(1)
def findMinMax(arr):
  min = arr[0]
  max = arr[0]
  
  for i in range(1, len(arr)):
    if arr[i] < min:
      min = arr[i]
    elif arr[i] > max:
      max = arr[i]
      
  return min, max

print(findMinMax([1, 2, 3, 4, 5, 6])) # (1, 6)
print(findMinMax([1, 2, 3, 4, 5, 6, 0])) # (0, 6)