# Given a T[] one-dimensional array of integers, we want to sort it in O(N) running time, without extra-memory
# The array can contain values: 0, 1 and 2 (3 different values). Edsger Dijkstra's problem.
# [0,1,2,1,2,0,0] => [0,0,0,1,1,2,2]

def sort(nums, pivot=1):
  leftSideIndex = 0
  actualItemIndex = 0
  rightSideIndex = len(nums)-1

  while actualItemIndex <= rightSideIndex:
    if (nums[actualItemIndex] < pivot):
      nums[actualItemIndex], nums[leftSideIndex] = nums[leftSideIndex], nums[actualItemIndex]
      leftSideIndex+=1
      actualItemIndex+=1
    elif (nums[actualItemIndex] > pivot):
      nums[actualItemIndex], nums[rightSideIndex] = nums[rightSideIndex], nums[actualItemIndex]
      rightSideIndex -= 1
    else:
      actualItemIndex += 1
    
  return nums

if __name__ == '__main__':
  print(sort([0,1,2,1,2,0,0]))