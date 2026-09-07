class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        nominations = []
        sum = 0

        self.calculate(sum, nominations, candidates, result, target)
        
        return result


    def calculate(self, sum, nominations, candidates, result, target):
        nominations.sort()
        if sum == target and nominations not in result:
            result.append(nominations)

        if sum < target:
            for c in candidates:
                self.calculate(sum+c, nominations + [c], candidates, result, target)    