# given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#   1. Open brackets must be closed by the same type of brackets.
#   2. Open brackets must be closed in the correct order.
# Example 1: input: s = "()" output: true
# Example 2: input: s = "()[]{}" output: true
# Example 3: input: s = "(]" output: false

def valid_parenthesis(s: str) -> bool:
  stack = []

  for char in s:
    if char == '(' or char == '[' or char == '{':
      stack.append(char)
    elif stack == []:
      return False
    elif char == ')' and stack.pop() != '(':
      return False
    elif char == ']' and stack.pop() != '[':
      return False
    elif char == '}' and stack.pop() != '{':
      return False

  return stack == []

print("(): ", valid_parenthesis("()"))
print("((: ", valid_parenthesis("(("))
print(")): ", valid_parenthesis("))"))
print("()[]{}: ", valid_parenthesis("()[]{}"))
print("(]: ", valid_parenthesis("(]"))
print("([)]: ", valid_parenthesis("([)]"))

