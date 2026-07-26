class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        
        target = nums_sum // 2


        stack = []
        def helper(i):
            if sum(stack) == target:
                return True
            
            if i >= len(nums):
                return False
            
            stack.append(nums[i])
            if helper(i+1):
                return True
            stack.pop()
            if helper(i+1):
                return True

            return False
        
        return helper(0)

        