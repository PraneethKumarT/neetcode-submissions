class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        maxList = []
        
        maxElem = 0
        for i in range(k):
            if nums[maxElem] <= nums[i]:
                maxElem = i
                    
        maxList.append(nums[maxElem])

        for i in range(k, len(nums)):
            if maxElem>=i-k+1:
                if nums[maxElem] <= nums[i]:
                    maxElem = i      
            else:
                maxElem = i-k+1
                for j in range(i-k+1, i+1):
                    if nums[maxElem] <= nums[j]:
                        maxElem = j
            
            maxList.append(nums[maxElem])
       
        
        return maxList
        