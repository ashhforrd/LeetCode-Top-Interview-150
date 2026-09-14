class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, nominations = [], []
        currSum = 0

        def calculate(currSum, nominations):
            nominations.sort()
            if currSum == target and nominations not in result:
                result.append(nominations)

            if currSum < target:
                for c in candidates:
                    calculate(currSum + c, nominations + [c])

        calculate(currSum, nominations)
        
        return result