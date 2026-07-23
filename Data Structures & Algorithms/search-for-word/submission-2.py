class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
            #helper
        def helper(i, j, match):

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[match]:
                return False

            if match == len(word)-1 and board[i][j] == word[match]:
                return True
            
            temp = board[i][j]
            board[i][j] = "#" 
            found = helper(i+1, j, match+1) or helper(i, j+1, match+1) or helper(i-1, j, match+1) or helper(i, j-1, match+1)
    
            board[i][j] = temp
            return found

        # search where it begins with str[0]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if helper(i, j, 0):
                        return True
        





        return False

