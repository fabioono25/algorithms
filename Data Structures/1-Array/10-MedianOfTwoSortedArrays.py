# given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# Time complexity: O(log(min(m,n))) - Space complexity: O(1)
# Example: nums1 = [1, 3], nums2 = [2] - Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2
# Example: nums1 = [1, 2], nums2 = [3, 4] - Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2+3)/2 = 2.5

def findMedianSortedArrays(nums1, nums2):
  if len(nums1) > len(nums2):
    nums1, nums2 = nums2, nums1 # if nums1 is larger than nums2, swap them. why? because we want to iterate over the smaller array
  
    # binary search necessary here
    