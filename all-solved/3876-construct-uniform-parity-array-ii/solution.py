class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()
        ln = len(nums1)
        nums2 = [0] * ln

        firstOdd = 0

        for n in nums1:
            if n % 2 == 1:
                firstOdd = n
                break
        
        # Membuat Ganjil Semua
        for i in range(ln):
            num = 0
            if nums1[i] % 2 == 1:
                num = nums1[i]
            else:
                num = nums1[i] - firstOdd
                if num < 1:
                    num = nums1[i]
            nums2[i] = num  

        isEven = all(n2 % 2 == 1 for n2 in nums2) 

        if isEven:
            return isEven          
        
        # Membuat Genap Semua
        nums2 = [0] * ln

        for j in range(ln):
            num = 0 
            if nums1[j] % 2 == 0:
                num = nums1[j]
            else:
                num = nums1[j] - firstOdd
                if num < 1:
                    num = nums1[j]
            nums2[j] = num
        
        isOdd = all(m2 % 2 == 0 for m2 in nums2)
        print(nums2)
        if isOdd:
            return isOdd
        
        return False
