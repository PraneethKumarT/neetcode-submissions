class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        curset = []
        subset = []

        def helper(nums, i, subset, curset, target):
            if sum(curset) == target:
                subset.append(curset.copy())
                return
            
            if i >= len(nums) or sum(curset) > target:
                return
            

            for j in range(i, len(nums)):
                curset.append(nums[j])
                helper(nums, j, subset, curset, target)
                curset.pop()

        helper(nums, 0, subset, curset, target)

        return subset
        