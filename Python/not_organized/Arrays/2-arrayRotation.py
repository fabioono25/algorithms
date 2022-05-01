''' 
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).


  A = [3, 8, 9, 7, 6]
  K = 3


    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
'''

def solution(A, K): #O(1)

    #if length of the array is equal the K number, we don't need to iterate    
    if (len(A) == 0 or len(A) == K):
        return A

    #validate if I should iterate more than once in the array (not necessary) 
    iterations = K % len(A)

    firstItemsArray = A[iterations * -1:]
    rotatedArray = firstItemsArray + A[:iterations * -1]

    return rotatedArray

solution([3, 8, 9, 7, 6], 3)
solution([5, -1000], 1)
solution([1, 1, 2, 3, 5], 42)
solution([], 1)