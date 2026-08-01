class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = deque()

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        direction = [
            [0, 1],
            [0, -1],
            [+1, 0],
            [-1, 0]
        ]
        cnt = 0
        while len(q) > 0:
            cnt += 1
            for i in range(len(q)):
                r, c = q.popleft()

                for d in direction:
                    new_r = r+d[0]
                    new_c = c+d[1]

                    if min(new_r, new_c) >= 0 and new_r < ROWS and new_c <COLS:
                        if grid[new_r][new_c] == 2147483647:
                            grid[new_r][new_c] = cnt
                            q.append((new_r, new_c))

        

        

                
        