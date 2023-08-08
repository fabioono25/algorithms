# Verify if a string is a palindrome
# examples: radar, madam

def isPalindrome(string):
  start_index = 0
  end_index = len(string)-1

  while end_index > start_index:
    if (string[start_index] != string[end_index]):
      return False

    start_index += 1
    end_index -= 1

  return True

def isPalindromeSimpler(s):
  if s == s[::-1]:
    return True
  return False

if __name__ == '__main__':
  print(f"madam is palindrome? {isPalindrome('madam')}")
  print(f"maddam is palindrome? {isPalindrome('maddam')}")
  print(f"madeam is palindrome? {isPalindrome('madeam')}")
  print(f"car is palindrome? {isPalindrome('car')}")

  print(f"madam is palindrome? {isPalindromeSimpler('madam')}")
  print(f"maddam is palindrome? {isPalindromeSimpler('maddam')}")
  print(f"madeam is palindrome? {isPalindromeSimpler('madeam')}")  
  print(f"car is palindrome? {isPalindromeSimpler('car')}")