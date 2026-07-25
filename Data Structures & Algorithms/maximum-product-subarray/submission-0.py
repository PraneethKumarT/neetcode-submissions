class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            if n == 0:
                currMin, currMax = 1, 1
                continue
            
            minVal = min(n, currMin*n, currMax*n)
            maxVal = max(n, currMin*n, currMax*n)
            currMin = minVal
            currMax = maxVal
            res = max(res, currMin, currMax)
        
        return res

"""


if 0: reset
if - and -
"""