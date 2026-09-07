class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        safe = set()

        for prereq in prerequisites:
            course, requisite = prereq
            adj[course].append(requisite)
    
        def dfs(j, visit):
            if j in visit:
                return False
            
            if j in safe:
                return True

            visit.add(j)

            for k in adj[j]:
                if dfs(k, visit) == False:
                    return False
                
            visit.remove(j)
            safe.add(j)
            return True

        for i in range(numCourses):
            visit = set()

            if dfs(i, visit) == False:
                return False
                
        return True