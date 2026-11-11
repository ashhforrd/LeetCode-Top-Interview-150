class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        minSum = right

        while left <= right:
            mid = (left + right) // 2

            def countSub(mid):
                sub = 1
                currSum = 0

                for n in nums:
                    if currSum + n > mid:
                        sub += 1
                        currSum = n
                    else:
                        currSum += n
                
                return sub

            subs = countSub(mid)

            if subs <= k:
                minSum = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return minSum
