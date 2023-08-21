# given 2 words or phrases, check if they are anagrams or not. Ex: "restful" and "fluster"
# another example of anagram, with duplicated letters: "aaabbbccc" and "abcabcabc"

# Time complexity: O(N) - Space complexity: O(N)
def is_anagram_hashmap(str1, str2):
  if len(str1) != len(str2):
    return False
  
  ret = {}
  for char in str1:
    if char in ret.keys():
      ret[char] += 1
    else:
      ret[char] = 1 

  for char in str2:
    if char in ret.keys():
      ret[char] -= 1
    else:
      return False

  return any(value == 0 for value in ret.values())

# Time complexity: O(N log N) - Space complexity: O(N)
def is_anagram_sorting(str1, str2):
  if len(str1) != len(str2):
    return False

  str1 = sorted(str1)
  str2 = sorted(str2)

  for i in range(len(str1)):
    if str1[i] != str2[i]:
      return False

  return True

# Time complexity: O(N log N) - Space complexity: O(N)
def is_anagram_sorting2(str1, str2):
  if len(str1) != len(str2):
    return False

  return sorted(str1) == sorted(str2)


print(is_anagram_hashmap("restful", "fluster"))  
print(is_anagram_hashmap("aaabbbccc", "abcabcabc"))
print(is_anagram_hashmap("aaabbbccc", "abcabcasbc"))

print(is_anagram_sorting("restful", "fluster"))
print(is_anagram_sorting("aaabbbccc", "abcabcabc"))
print(is_anagram_sorting("aaabbbccc", "abcabcasbc"))

print(is_anagram_sorting2("restful", "fluster"))
print(is_anagram_sorting2("aaabbbccc", "abcabcabc"))
print(is_anagram_sorting2("aaabbbccc", "abcabcasbc"))