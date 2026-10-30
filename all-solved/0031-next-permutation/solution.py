class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        j = len(nums)

        while i >= 0:
            if nums[i] < nums[i+1]:
                
                # ini cari angka terkecil dan masih kebih besar dari i
                j_idx_to_swap = -1
                min_num = 100
                for j in range(len(nums)-1, i, -1):
                    if nums[j] < min_num and nums[j] > nums[i]:
                        j_idx_to_swap = j
                        min_num = nums[j]
                
                # swap idx i dengan idx j
                num1 = nums[i]
                num2 = nums[j_idx_to_swap]
                
                nums[i] = num2
                nums[j_idx_to_swap] = num1

                nums[i+1:] = nums[i+1:][::-1]

                return


            i -= 1
        
        nums.reverse()



        # found = False

        # for i in range(len(nums)-2, -1, -1):
        #     if nums[i] < nums[i+1]:
        #         found = True
        #         min_num = 100
        #         idx_min = 0
        #         for i in range(len(nums) - 1, i, -1):
        #             # nums setelah index i dicari yang paling minimal dan lebih besar dari nums[i]
        #             if nums[j] > nums[i]:
        #                 num1 = nums[i]
        #                 num2 = nums[j]

        #                 nums[i] = num2
        #                 nums[j] = num1
                

        # if not found:
        #     nums = nums.reverse()
