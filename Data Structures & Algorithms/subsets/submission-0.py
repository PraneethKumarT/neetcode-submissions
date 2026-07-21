class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        currset = []


        def helper(nums, subset, currset, i):

            if i >= len(nums):
                subset.append(currset.copy())
                return


            currset.append(nums[i])
            helper(nums, subset, currset, i+1)

            currset.pop()
            helper(nums, subset, currset, i+1)

        
        helper(nums, subset, currset, 0)

        return subset


"""
 [1,2,3]

"""