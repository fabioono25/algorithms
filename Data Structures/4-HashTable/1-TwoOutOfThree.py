# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least #two out of the three arrays. 
# You may return the values in any order.
# Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
# Output: [3,2]
# Explanation: The values that are present in at least two arrays are:
# - 3, in all three arrays.
# - 2, in nums1 and nums2.

from typing import List 

# Time Complexity: O(n) - Space Complexity: O(n)
def TwoOutOfThree(nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
  hashTable = {}

  # I need the unique values of nums1, nums2, and nums3. Give me an example:
  nums1Distinct = set(nums1)
  nums2Distinct = set(nums2)
  nums3Distinct = set(nums3)

  for num in nums1Distinct:
    if num not in hashTable:
      hashTable[num] = 1
    else:
      hashTable[num] += 1
  
  for num in nums2Distinct:
    if num not in hashTable:
      hashTable[num] = 1
    else:
      hashTable[num] += 1
  
  for num in nums3Distinct:
    if num not in hashTable:
      hashTable[num] = 1
    else:
      hashTable[num] += 1
  
  returnList = []
  for key in hashTable:
    if hashTable[key] >= 2:
      returnList.append(key)
  
  return returnList

# Time Complexity: O(n) - Space Complexity: O(n)
def TwoOutOfThree2(nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
  common = set()

  for num in nums1:
    if num in nums2 or num in nums3:
      common.add(num)
  
  for num in nums2:
    if num in nums1 or num in nums3:
      common.add(num)

  for num in nums3:
    if num in nums1 or num in nums2:
      common.add(num)
  
  return list(common)

# Time Complexity: O(n) - Space Complexity: O(n) - best choice until now
def TwoOutOfThree3(nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
  output = []
  for num in nums1:
    if num in nums2 or num in nums3:
      if num not in output:
        output.append(num)

  for num in nums2:
    if num in nums1 or num in nums3:
      if num not in output:
        output.append(num)

  return output      

print(TwoOutOfThree([1,1,3,2], [2,3], [3])) # => [3,2]
print(TwoOutOfThree([3,1], [2,3], [1,2])) # => [1,2,3]
print(TwoOutOfThree([1,2,2], [4,3,3], [5])) # => []

print(TwoOutOfThree2([1,1,3,2], [2,3], [3])) # => [3,2]
print(TwoOutOfThree2([3,1], [2,3], [1,2])) # => [1,2,3]
print(TwoOutOfThree2([1,2,2], [4,3,3], [5])) # => []

print(TwoOutOfThree3([1,1,3,2], [2,3], [3])) # => [3,2]
print(TwoOutOfThree3([3,1], [2,3], [1,2])) # => [1,2,3]
print(TwoOutOfThree3([1,2,2], [4,3,3], [5])) # => []