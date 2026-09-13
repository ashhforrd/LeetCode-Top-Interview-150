class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        order = []

        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        safe, visiting = set(), set()
        
        def dfs(i):
            if i in safe:
                return True
            if i in visiting:
                return False

            visiting.add(i)
            for j in graph[i]:
                if dfs(j) == False:
                    return False
            
            visiting.remove(i)
            safe.add(i)
            order.append(i)

            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        
        return order
