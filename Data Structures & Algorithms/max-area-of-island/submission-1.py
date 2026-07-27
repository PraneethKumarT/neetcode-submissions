class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROW, COL = len(grid), len(grid[0])
        neig = [
            [+1, 0],
            [-1, 0],
            [0, +1],
            [0, -1]
        ]

        def dfs(r, c):
            if min(r,c) < 0 or (r>=ROW) or (c>=COL) or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1
            for d in neig:
                area += dfs(d[0] + r, d[1] + c)
            
            return area
        

        ans = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    ans = max(area, ans)
        
        return ans


            