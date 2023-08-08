# Reversing an array in O(N) linear time complexity (no additional memory used)
# [1,2,3,4,5,6] => [6,5,4,3,2,1]

def reverse(nums):
  start_index = 0
  end_index = len(nums)-1

  while end_index > start_index:
    nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
    start_index += 1
    end_index -= 1
  return nums

if __name__ == '__main__':
  print(reverse([1,2,3,4,5,6]))