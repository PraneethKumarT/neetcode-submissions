class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])


        direction = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]


        def dfs(r, c, ans):
            if min(r, c) < 0 or r >= ROWS or c >= COLS:
                return False

            for d in direction:
                new_r = r+d[0]
                new_c = c+d[1]

                if min(new_r, new_c) >= 0 and new_r < ROWS and new_c < COLS and heights[new_r][new_c] >= heights[r][c] and visited[new_r][new_c] == 0:
                    ans.add((new_r, new_c))
                    visited[new_r][new_c] = 1
                    dfs(new_r, new_c, ans)

        ans1 = set() 
        visited = [[0] * COLS for _ in range(ROWS)]

        for c in range(COLS):
            if visited[0][c] == 0:
                ans1.add((0,c))
                dfs(0, c, ans1)

        for r in range(ROWS):
            if visited[r][0] == 0:
                ans1.add((r,0))
                dfs(r, 0, ans1)
        
        ans2 = set()
        visited = [[0] * COLS for _ in range(ROWS)]

        for c in range(COLS):
            if visited[ROWS-1][c] == 0:
                ans2.add((ROWS-1, c))
                dfs(ROWS-1, c, ans2)

        for r in range(ROWS):
            if visited[r][COLS-1] == 0:
                ans2.add((r, COLS-1))
                dfs(r, COLS-1, ans2)
        
        return [list(cell) for cell in (ans1 & ans2)]