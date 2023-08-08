# Palindrome is a string that reads the same from left to right and from right to left
# e.g. "aba", "abba", "racecar", "madam"

# Solution 1: Two pointers - O(n) time | O(1) space
def isPalindrome1(s):
  low_index, high_index = 0, len(s) - 1
  while low_index < high_index:
    if s[low_index] != s[high_index]:
      return False
    low_index += 1
    high_index -= 1
  return True

# Solution 2: using recursion - O(n) time | O(n) space
def isPalindrome2(s):
  if len(s) <= 1:
    return True
  if s[0] != s[-1]:
    return False

  return isPalindrome2(s[1:-1])

# Solution 3: O(n) time | O(1) space


print('racecar: ', isPalindrome1("racecar"))
print('racecars: ', isPalindrome1("racecars"))
print('racecar: ', isPalindrome2("racecar"))
print('racecars: ', isPalindrome2("racecars"))
