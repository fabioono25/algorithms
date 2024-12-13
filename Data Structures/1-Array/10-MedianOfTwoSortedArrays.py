# given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# Time complexity: O(log(min(m,n))) - Space complexity: O(1)
# Example: nums1 = [1, 3], nums2 = [2] - Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2
# Example: nums1 = [1, 2], nums2 = [3, 4] - Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2+3)/2 = 2.5

def findMedianSortedArrays(nums1, nums2):
  if len(nums1) > len(nums2):
    nums1, nums2 = nums2, nums1 # if nums1 is larger than nums2, swap them. why? because we want to iterate over the smaller array
  
  total = len(nums1) + len(nums2)
  half = total // 2
    
  # binary search on the smaller array
  left, right = 0, len(nums1) - 1
  
  # compute the middle value
  while True: 
    i = (left + right) // 2
    j = half - i - 2
  
    nums1Left = nums1[i] if i >= 0 else float('-inf')
    nums1Right = nums1[i + 1] if (i + 1) < len(nums1) else float('inf')
    nums2Left = nums2[j] if j >= 0 else float('-inf')
    nums2Right = nums2[j + 1] if (j + 1) < len(nums2) else float('inf')
    
    if nums1Left <= nums2Right and nums2Left <= nums1Right:
      if total % 2 == 0:
        return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2
      else:
        return min(nums1Right, nums2Right)
    elif nums1Left > nums2Right:
      right = i - 1
    else:
      left = i + 1
        
print(findMedianSortedArrays([1, 3], [2])) # 2.0
print(findMedianSortedArrays([1, 2], [3, 4])) # 2.5