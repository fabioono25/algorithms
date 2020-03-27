mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

print(mylist[0]) # is 'a'

print(mylist[0:1]) # is also 'a'

print(mylist[1:1]) # is [] (empty) because "to" excludes the index you enter so it cannot be the same as "from"

# If "from" is 2 it will start at index 2. Since indexes start at 0 (0,1,2,3,...) it will be the 3rd item of the array.

#If "to" is 3 it will stop at index 2. So mylist[2:3] only gives the value of index 2.

print(mylist[5:]) #  will give you the entries from index 5 to the end > ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

print(mylist[:5]) #  will give you the entries from the beginning to index 4 (since 5 will be excluded) > ['a', 'b', 'c', 'd', 'e']

print(mylist[-1:]) #  will give you the last entry in the list because negative numbers start at the end

print(mylist[-4:]) #  will start at 4th from last and end at the last entry > ['j', 'k', 'l', 'm']

print(mylist[5:-4]) #  will start at index 5 and end at 4th from last > ['f', 'g', 'h', 'i']

#Now for the optional argument:

print(mylist[::]) #  is the same as mylist[:] and mylist[::1] since it will give the whole array

print(mylist[::2]) #  has step = 2 so it will take one every 2 from the array > ['a', 'c', 'e', 'g', 'i', 'k', 'm']

print(mylist[1::2]) #  will start taking every two entries from index 1 (second entry) > ['b', 'd', 'f', 'h', 'j', 'l']

print(mylist[::-1]) #  has step = -1 so it will output the whole array but in reverse order > ['m', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

print(mylist[::-2]) #  will take one every two starting at the end in reverse order > ['m', 'k', 'i', 'g', 'e', 'c', 'a']

print(mylist[-8:1:-1]) #  when having a negative step (-1) your first argument will start at the "right side" and go down to the left. In this example remember that "to" is excluded but this time being in reverse order it will stop at index 2. > ['f', 'e', 'd', 'c']

