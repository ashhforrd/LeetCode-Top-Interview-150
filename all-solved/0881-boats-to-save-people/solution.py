class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        boats = 0

        people.sort()
        left, right = 0, len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            
            boats += 1
            right -= 1
        
        return boats
