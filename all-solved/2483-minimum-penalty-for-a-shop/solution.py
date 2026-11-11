class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count('Y')
        minPenalty = penalty
        best = 0

        for i in range(len(customers)):
            if customers[i] == 'Y':
                penalty -= 1
            else:
                penalty += 1
            
            if penalty < minPenalty:
                best = i + 1
                minPenalty = penalty

        return best
