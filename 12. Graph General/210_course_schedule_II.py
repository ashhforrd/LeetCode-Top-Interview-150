class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        output = []

        for p in prerequisites:
            a, b = p
            adj[a].append(b)
        
        visit, cycle = set(), set()

        def dfs(course):
            if course in visit:
                return True
            if course in cycle:
                return False
            
            cycle.add(course)
            for c in adj[course]:
                if dfs(c) == False:
                    return False
            
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output