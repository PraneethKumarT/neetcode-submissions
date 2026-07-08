class Solution:

    def hourReq(self, piles, k):
        return sum(math.ceil(p/k) for p in piles)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minAnswer = max(piles)

        while l <=r:
            mid = (l+r)//2

            hoursReq = self.hourReq(piles, mid)
            if hoursReq <= h:
                minAnswer = mid
                r = mid-1
            else:
                l = mid+1

        
        return minAnswer
        

"""
[1. max(p)lk]
"""