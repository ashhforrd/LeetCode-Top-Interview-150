class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        string_map = {}

        for i in range(len(s)):
            if s[i] not in string_map:
                string_map[s[i]] = t[i] if t[i] not in string_map.values() else ""
            
            if t[i] != string_map[s[i]]:
                return False
        
        return True