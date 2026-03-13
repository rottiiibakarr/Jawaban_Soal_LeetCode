nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

m = 3
n = 3 

def merge(nums1, m, nums2, n) :
  p1 = m - 1 # Contoh 2 
  p2 = n - 1 # Contoh 2
  p = (m + n) - 1 # (3 + 3) - 1 = 5 
  
  while p2 >= 0 : # Melakukan perulangan
    if p1 >= 0 and nums1[p1] > nums2[p2] : #nums1[p1] = 3, nums2[p2] = 6
      nums1[p] = nums1[p1]
      p1 -= 1 #
    else :
      nums1[p] = nums2[p2]
      p2 -= 1 
    
    p -= 1

merge(nums1, m, nums2, n)

print(nums1)