class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)

        for edge in edges:
            src, dst = edge
            graph[src].append(dst)
            graph[dst].append(src)

        visiting, safe = set(), set()

        def dfs(src):
            if src == destination:
                return True

            if src in visiting:
                return
            
            visiting.add(src)
            for dst in graph[src]:
                if dfs(dst) == True:
                    return True
        
        return dfs(source) or False
