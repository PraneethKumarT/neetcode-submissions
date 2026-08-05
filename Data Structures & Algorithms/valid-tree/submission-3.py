class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = defaultdict(list)

        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        
        visited = [False] * n
        pathVisited =  [False] * n
    

        def dfs(src, parent):
            if pathVisited[src]:
                return False
            
            if visited[src]:
                return True
            
            visited[src] = True
            pathVisited[src] = True

            for nei in adj[src]:
                if nei == parent:
                    continue
                if not dfs(nei, src):
                    return False
            
            pathVisited[src] = False
            return True
        
        if not dfs(0, -1):
            return False
        
        return sum(visited) == n
        