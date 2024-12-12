# [1, 2, 3, 4, 5] with a left rotation of 2 becomes [3, 4, 5, 1, 2]
# why: 1, 2 are the first two elements of the list, so they are moved to the end of the list
# given a list and a number of left rotations, return the list after the rotations

# Time Complexity: O(N) - Space Complexity: O(N)
def left_rotation(list, rotations):
  result = []
  for i in range(rotations, len(list)):
    result.append(list[i])
  for i in range(0, rotations):
    result.append(list[i])
  return result

# Time Complexity: O(N) - Space Complexity: O(1)
def left_rotation_in_place(list, rotations):
  for _ in range(rotations):
    list.append(list.pop(0))
  return list

# using the same array. Time Complexity: O(N) - Space Complexity: O(1)
def left_rotation_in_place2(list, rotations):
  rotations = rotations % len(list)
  list[:] = list[rotations:] + list[:rotations] 
  # why list[:] instead of list =? because list = creates a new reference to the list, while list[:] modifies the original list
  return list

print(left_rotation([1, 2, 3, 4, 5], 2)) # [3, 4, 5, 1, 2]
print(left_rotation_in_place([1, 2, 3, 4, 5], 2)) # [3, 4, 5, 1, 2]
print(left_rotation_in_place2([1, 2, 3, 4, 5], 2)) # [3, 4, 5, 1, 2]
