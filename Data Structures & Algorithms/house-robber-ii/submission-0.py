class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        cache = [-1] * len(nums)
        def helper(i, end):
            if i > end:
                return 0
            
            if cache[i] != -1:
                return cache[i]

            cache[i] = max(nums[i] + helper(i+2, end), helper(i+1, end))
            return cache[i]
        
        res1 = helper(0, len(nums) - 2)
        cache = [-1] * len(nums)
        res2 = helper(1, len(nums) - 1)

        return max(res1, res2)
        