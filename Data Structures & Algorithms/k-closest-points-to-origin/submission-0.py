class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []

        for x, y in points:
            dist = x**2 + y**2

            heapq.heappush(maxheap, (-dist, (x,y)))
            while len(maxheap) > k:
                heapq.heappop(maxheap)
        
        ans = []
        for x, y in maxheap:
            ans.append([y[0], y[1]])
        
        return ans



        