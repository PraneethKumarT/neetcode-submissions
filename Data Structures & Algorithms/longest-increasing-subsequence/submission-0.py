class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(len(nums)-1, -1, -1):
            j = i
            while j < len(nums):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                j+=1

        return max(dp)