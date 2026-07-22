class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def helper(subset, currset, i, nums, target):
            
            if sum(currset) == target:
                subset.append(currset.copy())
                return

            if i>= len(nums) or sum(currset) > target:
                return

            currset.append(nums[i])
            helper(subset, currset, i+1, nums, target)
            currset.pop()

            # 2. Skip identical numbers before making the EXCLUDE call
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(subset, currset, i+1, nums, target)
        
        subset = []
        currset = []
        helper(subset, currset, 0, candidates, target)
        return subset