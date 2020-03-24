# python arrays.py - Operations with arrays:

# Python doesn't have an array data structure, but has a list, which is a collection of items

numbers = [1,2,3,4,'e',5]

# random indexing --> O(1) get the items if we know the index
print(numbers[0]); #1
print(numbers[4]); #e

numbers[1] = 200

print(numbers[1]); #200

for number in numbers:
    print(number) #print all numbers

#using indexes
for i in range(len(numbers)):
    print(numbers[i])

#return list of items
print(numbers[0:2])    #[1, 200]

print(numbers)         #[1, 200, 3, 4, 'e', 5] 
print(numbers[:])      #[1, 200, 3, 4, 'e', 5] 
print(numbers[:-1])    #[1, 200, 3, 4, 'e']
print(numbers[:-2])    #[1, 200, 3, 4]


numbers[4] = 201;
#find the maximum value
maximum = numbers[0]

for num in numbers: #linear search - O(n)
    if num > maximum:
        maximum = num

print("Max value is", maximum, ".")

shopping = ['butter', 'bread']
shopping += ["eggs"]

print(shopping) #['butter', 'bread', 'eggs']

#The only difference is that range returns a Python list object and xrange returns an xrange object. ... 
# It means that xrange doesn't actually generate a static list at run-time like range does.

repetition = ['hey']

print (repetition * 3) #['hey', 'hey', 'hey']

print([1, 2, 3] + [4, 5, 6] == [1, 2, 3, 4, 5, 6]) #True

print('butter' in ['bread', 'butter', 'cheese']) #True

reversed = ['bread', 'butter', 'cheese']
reversed.reverse()
print(reversed) #['cheese', 'butter', 'bread']