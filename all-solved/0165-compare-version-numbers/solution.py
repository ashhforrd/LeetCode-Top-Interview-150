class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # ver1, ver2 = "0", "0"
        # i, j = 0, 0
        # n1, n2 = len(version1), len(version2)

        # while i < n1 and j < n2:

        #     while i < n1 and version1[i] != ".":
        #         ver1 += version1[i]
        #         i += 1

        #     while j < n2 and version2[j] != ".":
        #         ver2 += version2[j]
        #         j += 1
                                    
        #     if int(ver1) < int(ver2):
        #         return -1
        #     elif int(ver1) > int(ver2):
        #         return 1
            
        #     ver1, ver2 = "0", "0"
            
        #     i += 1
        #     j += 1
                
        # while i < n1:
        #     if version1[i] != ".":
        #         ver1 += version1[i]
        #     i += 1
        
        # while j < n2:
        #     if version2[j] != ".":
        #         ver2 += version2[j]
        #     j += 1
                
        # if int(ver1) < int(ver2):
        #     return -1
        # elif int(ver1) > int(ver2):
        #     return 1
        
        # return 0

        v1, v2 = version1.split('.'), version2.split('.')
        n = max(len(v1), len(v2))

        for i in range(n):
            a = int(v1[i] if i < len(v1) else 0)
            b = int(v2[i] if i < len(v2) else 0)
        
            if a < b:
                return -1
            if a > b:
                return 1
        
        return 0
