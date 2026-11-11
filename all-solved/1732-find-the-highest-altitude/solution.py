class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        highest = 0
        altitude = 0

        for n in gain:
            highest = max(highest, altitude)
            altitude += n
        
        highest = max(highest, altitude)

        return highest
