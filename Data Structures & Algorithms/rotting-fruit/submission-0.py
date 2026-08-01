class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        ROW, COL = len(grid), len(grid[0])
        fresh = 0

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1


        direction = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]
        cnt = 0
        while len(q) > 0 and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for d in direction:
                    new_r = r + d[0]
                    new_c = c + d[1]

                    if min(new_r, new_c) >= 0 and new_r < ROW and new_c < COL:
                        if grid[new_r][new_c] == 1:
                            q.append((new_r, new_c))
                            grid[new_r][new_c] = 2
                            fresh -=1 
            cnt += 1

        return cnt if fresh == 0 else -1