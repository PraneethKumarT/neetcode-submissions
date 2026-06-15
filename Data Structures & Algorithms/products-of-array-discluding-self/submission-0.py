class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n

        temp = 1 
        for i in range(n):
            prefix[i] = temp
            temp = temp * nums[i]
        
        temp = 1
        for i in range(n-1, -1, -1):
            postfix[i] = temp
            temp = temp * nums[i]
        
        return [a*b for a,b in zip(prefix, postfix)]

    
"""
input : [1,2,4,6]
prefix:    [1,1,2,8] 
postfix:   [48,24,6,1]
prefix*postfix
output: [48,24,12,8]
    
""" 