nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

m = 3
n = 3 

def merge(nums1, m, nums2, n) :
    nums1[m:] = nums2
    nums1.sort()

merge(nums1, m, nums2, n)

print(nums1)