class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            long = 1
            if int(num-1) not in num_set:
                temp_num = num+1
                while temp_num in num_set:
                    long += 1
                    temp_num += 1
            
            longest = max(long, longest)
        
        return longest



"""
input: nums = [2,20,4,10,3,4,5]



output = 4 (2,3,4,5)
"""