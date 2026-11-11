class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0

        for i in range(n):
            if i not in visited:
                provinces += 1
                visited.add(i)
           
                q = deque()
                q.append(i)

                while q:
                    r = q.popleft()

                    for j in range(n):
                        if isConnected[r][j] == 1 and j not in visited:
                            visited.add(j)
                            q.append(j)
        
        return provinces

# [[1,1,0],
# [1,1,0],
# [0,0,1]]
