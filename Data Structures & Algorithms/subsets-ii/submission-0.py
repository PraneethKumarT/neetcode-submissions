class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        def helper(subset, currset, nums, i):
            if i >= len(nums):
                subset.append(currset.copy())
                return
            
            currset.append(nums[i])
            helper(subset, currset, nums, i+1)
            currset.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i+=1
            helper(subset, currset, nums, i+1)
        
        subset = []
        currset = []
        helper(subset, currset, nums, 0)

        return subset
        