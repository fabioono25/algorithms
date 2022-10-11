# Given n non-negative integers representing an elevation map where the width of each bar is 1. Compute how much water it can trap after raining!
# Example: given [4,1,3,1,5], the result is 7 (all spaces between the highest columns)
#         1
# 1 0 0 0 1
# 1 0 1 0 1
# 1 0 1 0 1
# 1 1 1 1 1

def trappingRainWater(heights):
  if len(heights) < 3:
    return 0
  
  left_max = [0 for _ in range(len(heights))]
  right_max = [0 for _ in range(len(heights))]

  for i in range(1, len(heights)):
    left_max[i] = max(left_max[i-1], heights[i-1])

  for i in range(len(heights) - 2, -1, -1):
    right_max[i] = max(right_max[i+1], heights[i+1])

  trapped = 0
  for i in range(1, len(heights)-1):
    if (min(left_max[i], right_max[i]) > heights[i]):
      trapped += min(left_max[i], right_max[i]) - heights[i]
  
  return trapped

if __name__ == '__main__':
  print(f'water trapped in [4,1,3,1,5]: {trappingRainWater([4,1,3,1,5])}')
  print(f'water trapped in [1,0,2,1,3,1,2,0,3]: {trappingRainWater([1,0,2,1,3,1,2,0,3])}')