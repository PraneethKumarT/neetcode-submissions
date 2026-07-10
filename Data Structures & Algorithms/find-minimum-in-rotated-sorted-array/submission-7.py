class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]
        low, high = 0, len(nums)-1
        
        while low < high:
            mid = (low+high)//2

            if nums[mid] > nums[high]:
                low = mid+1
            else:
                high = mid 
        
        return nums[low]
        


"""

numbers are unique
min element - O(logn)

        0 1 2 3 4 5
input: [3,4,5,6,1,2]. 


Record min and search the unsorted split
mid > low - search right
mid < high - search left
"""