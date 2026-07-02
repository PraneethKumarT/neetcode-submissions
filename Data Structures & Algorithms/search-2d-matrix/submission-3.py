class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        possibleRow = []
        #step 1: Indetify which row
        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                possibleRow = row
        
        # if len(possibleRow) == 0:
        #     return False

        #step 2: Search within that row
        return self.search(possibleRow, target)
    
    def search(self, row, target):

        low, high = 0, len(row)-1

        while low <= high:
            mid = (low+high)//2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                high = mid-1
            else:
                low = mid+1
        

        return False
    
    
        