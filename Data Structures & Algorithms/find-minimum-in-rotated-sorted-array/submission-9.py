class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        # Change to strictly less than, because when low == high, 
        # they are both pointing exactly at the minimum element.
        while low < high:
            mid = (low + high) // 2
            
            # If mid is greater than high, the minimum is in the right half
            if nums[mid] > nums[high]:
                low = mid + 1
            # Otherwise, mid itself could be the minimum, or it's to the left
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