# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1: Input: nums = [2,7,11,15], target = 9 Output: [0,1] Because nums[0] + nums[1] == 9, we return [0, 1].

from typing import List

# Solution 1 -  Brute Force - Time Complexity: O(n^2), Space Complexity: O(1)
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]
    return []


# Solution 2 - Hash Table - Time Complexity: O(n), Space Complexity: O(n)
def twoSum2(nums: List[int], target: int) -> List[int]:
    hashTable = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashTable:
            return [hashTable[complement], i]
        hashTable[nums[i]] = i
    return []

print(twoSum([2,7,11,15], 9))
print(twoSum2([2,7,11,15], 9))

