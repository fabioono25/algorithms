# Reverse a given integer
# 1234 => 4321

def reverseInteger(nums):
  reversed = 0
  remainder = 0

  while nums > 0:
    remainder = nums % 10
    nums //= 10
    reversed = reversed * 10 + remainder

  return reversed

if __name__ == '__main__':
  print(reverseInteger(1234))