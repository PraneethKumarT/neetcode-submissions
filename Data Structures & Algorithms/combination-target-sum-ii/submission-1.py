class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def helper(subset, currset, i, nums, target):
            
            if sum(currset) == target:
                subset.append(currset.copy())
                return

            if i>= len(nums) or sum(currset) > target:
                return

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                currset.append(nums[j])
                helper(subset, currset, j+1, nums, target)
                currset.pop()
        
        subset = []
        currset = []
        helper(subset, currset, 0, candidates, target)
        return subset