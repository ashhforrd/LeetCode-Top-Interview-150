class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        safe, visiting = set(), set()

        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
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
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True