class Solution:
    def rob(self, nums: List[int]) -> int:

        # cache = [-1] * len(nums)
        # def helper(i):
        #     if i >= len(nums):
        #         return 0

        #     if cache[i] != -1:
        #         return cache[i]

        #     # rob and go to next, or skip
        #     cache[i] = max(nums[i] + helper(i+2), helper(i+1))
        #     return cache[i]
    
        # return helper(0)

        ans = [0] * (len(nums)+2)

        for i in range(len(nums)-1, -1, -1):
            ans[i] = max(ans[i+1], nums[i] + ans[i+2])
        
        return ans[0]

    """

[1,2,3,4]. o/t: 6

        .
    1      2
3    4   4



    """