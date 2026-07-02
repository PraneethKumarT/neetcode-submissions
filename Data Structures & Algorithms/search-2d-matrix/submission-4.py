class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top = 0 
        bot = len(matrix) - 1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                possibleRow = matrix[row]
                break
        
        if not (top <= bot):
            return False
        
        return self.search(possibleRow, target)
    
    def search(self, row, target):
        low, high = 0 , len(row)-1

        while low <= high:
            mid = (low+high) // 2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                high = mid-1
            else:
                low = mid + 1 
        
        return False

        