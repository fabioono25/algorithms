# usually this is called an array, but in python it is called a list
# everything is an object in python, so you can store any type of data in a list
# if you want to use an array - you can use NumPy library
my_list = [1,2,3,4,5,6, "Test", 4.5]

print(432 % 10)
print(43 % 10)

print(my_list) # [1, 2, 3, 4, 5, 6]
print(my_list[0]) # 1
print(type(my_list)) # <class 'list'>

my_list[1] = 99 # [1, 99, 3, 4, 5, 6]

# delete an element
del my_list[0] # [99, 3, 4, 5, 6]

print(len(my_list)) # 5
print(my_list) # [99, 3, 4, 5, 6, 'Test', 4.5]

for item in my_list:
  print(item)

my_list.append(100)
my_list.append(100)

print(my_list)
print(my_list[-1]) # prints the last element in the list
print(my_list[-3]) # 4.5 prints the third element from the end of the list
print(my_list[0: 2]) # [99, 3]

print(50*'=')

list1 = [1,2,3]
list2 = [4,5,6]
result = list1 + list2 # concatenation
print(result) # [1, 2, 3, 4, 5, 6]
print(50*'=')

list1.extend(list2) # [1, 2, 3, 4, 5, 6]
print(list1) # [1, 2, 3, 4, 5, 6]
print(list2) # [4, 5, 6]

result3 = list1.copy()
print(result3) # [1, 2, 3, 4, 5, 6]

list1.remove(3)
print(list1) # [1, 2, 4, 5, 6]

result4 = list1.pop()
print(result4) # 6

result5 = list1.pop(2)
print(result5) # 4

list1.reverse()
print(list1) # [5, 2, 1]

listNames = ['Alex', 'John', 'Mary', 'Steve', 'Anna']
listNames.sort()
print(listNames) # ['Alex', 'John', 'Mary', 'Steve']

print(50*'=') 

# List Comprehension. What is it: it is a way to create a list in a more concise way
# [expression for item in list]
# [expression for item in list if condition]
# [expression for item in list if condition1 and condition2]

numbers = [1, -5, 6, 8, -4, 9, -3]

even_numbers = []

for num in numbers:
  if num % 2 == 0:
    even_numbers.append(num)

# using list comprehension
even_numbers2 = [num for num in numbers if num % 2 == 0] # explanation: for each number in numbers, if the number is even, add it to the list

names = ['Alex', 'John', 'Mary', 'Steve', 'Anna']

names_starting_a = [name for name in names if name.startswith('A')]

print(names_starting_a) # [6, 8, -4]

print(50*'=')

for name in names:
  print(name)
  
print(50*'=')

test = 'racecars'
print(test[::-1]) # sracecar

print(4 // 2)
print(5 // 2 )
print (5 / 2)