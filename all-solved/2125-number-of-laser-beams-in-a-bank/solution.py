class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        # lasers = []
        # for laser in bank:
        #     if laser.count("1") == 0:
        #         continue
        #     lasers.append(laser)

        # total = 0
        # for i in range(len(lasers) - 1):
        #     total += lasers[i].count("1") * lasers[i + 1].count("1")
        
        # return total

        prev = 0
        total = 0

        for laser in bank:
            current = laser.count('1')

            if current == 0:
                continue
            
            total += prev * current
            prev = current

        return total
