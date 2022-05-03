# the objective is to reverse an one-dimensional array of integers in linear time complexity O(n)
# no additional memory should be used
# example: input [1,2,3,4,5] then output is [5,4,3,2,1]

def reverse(numbers):
  startIndex = 0
  lastIndex = len(numbers)-1

  while startIndex < lastIndex:
    #swapping items here
    numbers[startIndex], numbers[lastIndex] = numbers[lastIndex], numbers[startIndex]
    startIndex+=1
    lastIndex-=1

  return numbers

result = reverse([1,2,3,4,5])
print(result)