class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set([])

        for i, num in enumerate(nums):
            res = self.twoSum(nums, i+1, -1*num, ans)

        return [list(triplet) for triplet in ans]
    
    def twoSum(self, nums, l, target, ans):
        r = len(nums) - 1

        while l<r:
            lnum = nums[l]
            rnum = nums[r]

            if lnum + rnum == target:
                ans.add(tuple(sorted([lnum, rnum, -1 * target])))
                l+=1
                r-=1
            elif lnum + rnum < target:
                l += 1
            else:
                r -= 1
        
