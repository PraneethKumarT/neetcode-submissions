class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = defaultdict(list)

        for dest, src in prerequisites:
            adj[src].append(dest)
        
        visited = [False] * numCourses
        pathVisited = [False] * numCourses
        stack = []

        def dfs(src):
                      
            if pathVisited[src]:
                return False
                
            if visited[src]:
                return True
  

            visited[src] = True
            pathVisited[src] = True
            for nei in adj[src]:
                if not dfs(nei):
                    return False

            pathVisited[src] = False
            stack.append(src)
            return True
        
        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return []
        
        return stack[::-1] if len(stack) == numCourses else []
            


        