# Reverse a given number. Ex: 4598 -> 8954

# Time complexity: O(N) - Space complexity: O(N)
def reverse_integer_first(n):
  # convert a number to an array of digits
  digits = []
  while n > 0: # O(N)
    digits.append(n % 10)
    n //= 10

  # convert an array of digits to a number
  result = 0
  for i in range(len(digits)): # O(N)
    result += digits[i] * (10 ** (len(digits) - i -1))

  print(result)

# Time complexity: O(log(N)) - Space complexity: O(1)
def reverse_integer_optimized(n):
  reversed_number = 0
  while n > 0:
    last_digit = n % 10
    reversed_number = (reversed_number * 10) + last_digit
    n //= 10

  print(reversed_number)

# Time complexity: O(log(N)) - Space complexity: O(log(N))
def reverse_integer_string_conversion(n):
  numstr = str(n)
  reversed_number = int(numstr[::-1])
  
  print(reversed_number)

reverse_integer_first(4598)
reverse_integer_optimized(4598)
reverse_integer_string_conversion(4598)
