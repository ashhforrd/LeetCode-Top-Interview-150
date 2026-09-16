class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStr = ["".join(sorted(s)) for s in strs]
        groups, visited = [], set()

        for i in range(len(strs)):
            group = []

            for j in range(i, len(strs)):
                if sortedStr[j] == sortedStr[i] and j not in visited:
                    group.append(strs[j])
                    visited.add(j)
            
            if group and group not in groups:
                groups.append(group)

        return groups
