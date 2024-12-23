# Find intersection of two unsorted arrays

arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6]

# Brutal force solution
# Time complexity: O(n*m) - Space complexity: O(n)


def findIntersection(arr1, arr2):
    intersection = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                intersection.append(arr1[i])
    return intersection

# using in operator (simular to brutal force solution)
# Time complexity: O(n*m) - Space complexity: O(n)


def findIntersection2(arr1, arr2):
    intersection = []
    for num in arr1:
        if num in arr2:
            intersection.append(num)
    return intersection

# better solution, using the set data structure
# Time complexity: O(n+m) - Space complexity: O(n)


def findIntersection3(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    return list(set1.intersection(set2))

# sorting and two pointers
# Time complexity: O(nlogn + mlogm) - Space complexity: O(1)


def findIntersection4(arr1, arr2):
    arr1.sort()
    arr2.sort()
    intersection = []
    ptr1 = 0
    ptr2 = 0

    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if arr1[ptr1] == arr2[ptr2]:
            intersection.append(arr1[ptr1])
            ptr1 += 1
            ptr2 += 1
        elif arr1[ptr1] < arr2[ptr2]:
            ptr1 += 1
        else:
            ptr2 += 1
            
    return intersection


print(findIntersection(arr1, arr2))  # [3, 5]
print(findIntersection2(arr1, arr2))  # [3, 5]
print(findIntersection3(arr1, arr2))  # [3, 5]
print(findIntersection4(arr1, arr2))  # [3, 5]
