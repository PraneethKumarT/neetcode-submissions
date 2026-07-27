class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROW, COL = len(grid), len(grid[0])
        def dfs(r, c):
            if min(r,c) < 0 or (r >= ROW) or (c >= COL) or vis[r][c] == 1 or grid[r][c] == "0":
                return False
            
            vis[r][c] = 1
            neighbours = [
                [-1,0],
                [+1, 0],
                [0, +1],
                [0, -1]
            ]
            for d in neighbours:
                new_row = d[0]+r
                new_col = d[1]+c
                
                if min(new_row, new_col) >= 0 and (new_row < ROW) and (new_col < COL) and grid[new_row][new_col] == "1" and vis[new_row][new_col] == 0:
                    dfs(new_row, new_col)
            
            return True
            
        vis = [[0] * COL for _ in range(ROW)]
        cnt= 0
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == "1" and vis[row][col] == 0:
                    dfs(row, col)
                    cnt+=1
        
        return cnt


        