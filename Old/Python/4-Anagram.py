# Verify if it is an anagram
# restful and fluster are anagrams

def isAnagram(str1, str2):
  dict = {}
  
  if (len(str1) != len(str2)):
    return False

  for str in str1:
    if str in dict.keys():
      dict[str] += 1
    else:
      dict[str] = 1

  for str in str2:
    if str in dict.keys():
      dict[str] -= 1
    else:
      return False

  return any(x == 0 for x in dict.values())

def isAnagramSorting(str1, str2):
  if (len(str1) != len(str2)):
    return False
  
  # O(n log n) operation
  str1 = sorted(str1)
  str2 = sorted(str2)

  return str1 == str2

if __name__ == '__main__':
  print(isAnagram('restful','fluster'))
  print(isAnagram('restful','flusters'))
  print(isAnagramSorting('restful','fluster'))
  print(isAnagramSorting('restful','flusters'))  