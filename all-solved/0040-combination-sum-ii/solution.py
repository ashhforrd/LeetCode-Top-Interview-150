class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        nominations = []
        index_used = 0
        sum = 0

        candidates.sort()

        self.calculate(sum, nominations, candidates, index_used, result, target)
        
        return result


    def calculate(self, sum, nominations, candidates, index_used, result, target):
        nominations.sort()
        if sum == target and nominations not in result:
            result.append(nominations)
        
        if sum > target:
            return

        if sum < target:
            for i in range(index_used, len(candidates)):
                if i > index_used and candidates[i] == candidates[i - 1]:
                    continue
                self.calculate(sum+candidates[i], nominations + [candidates[i]], candidates, i + 1, result, target)
