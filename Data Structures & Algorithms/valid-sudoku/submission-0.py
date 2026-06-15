class Solution:

    def helper(self, x, y, board):
        row = board[x]
        col = [board[r][y] for r in range(9)]

        start_row, start_col = x//3 * 3 , y//3 * 3
        subset = []
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                subset.append(board[r][c])

        # 3. Strip out the "." empty characters before checking uniqueness
        clean_row = [char for char in row if char != "."]
        clean_col = [char for char in col if char != "."]
        clean_sub = [char for char in subset if char != "."]
        
        # 4. Compare lengths to check for duplicates
        return len(set(clean_row)) == len(clean_row) and \
               len(set(clean_col)) == len(clean_col) and \
               len(set(clean_sub)) == len(clean_sub)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if(board[i][j] != "."):
                    if (self.helper( int(i), int(j), board) == False):
                        return False

        
        return True