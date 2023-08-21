# we need to reverse a list in O(N) time complexity

list = [1,2,3,4,5,6]

# Brute force approach - Time Complexity: O(N) - Space Complexity: O(N)
def solution1():
  result = []
  for item in range(len(list), 0, -1):
    result.append(item)
  return result

# In-Place reversal - Time Complexity: O(N) [it is an O(N/2) simplified to O(N)] - Space Complexity: O(1)
def solution2():
  low_index, high_index = 0, len(list) - 1
  while low_index < high_index:
    list[low_index], list[high_index] = list[high_index], list[low_index]
    low_index += 1
    high_index -= 1
  return list

# call the function
print(solution1())
print(solution2())
