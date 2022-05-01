#Given array A consisting of N integers, return the reversed array

#in python 2.x, xrange is used to return a generator while range is used to return a list. 
# In python 3.x , xrange has been removed and range returns a generator just like xrange in python 2.x. 
# Therefore, in python 3.x you need to use range rather than xrange.

#We can iterate over the first half of the array and exchange the elements with those in the second part of the array: 

def reverse(A):
    N = len(A)
    for i in range(N // 2):
        k = N - i - 1
        A[i], A[k] = A[k], A[i]
    return A

print(reverse([4,5,3,2,1,0,8])) #[8, 0, 1, 2, 3, 5, 4]