class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)

        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        
        visited = [False] * n

        def dfs(src, parent):
            if visited[src]:
                return
            
            visited[src] = True
            for nei in adj[src]:
                if nei != parent:
                    dfs(nei, src)
            return
        
        cnt = 0
        for i in range(n):
            if not visited[i]:
                cnt += 1
                dfs(i, -1)
        
        return cnt