class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = collections.defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        safe, visit = set(), set()
        order = []

        def dfs(i):
            if i in safe:
                return True

            if i in visit:
                return False
            
            visit.add(i)
            for j in graph[i]:
                if dfs(j) == False:
                    return False
            
            visit.remove(i)
            safe.add(i)
            order.append(i)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return order
