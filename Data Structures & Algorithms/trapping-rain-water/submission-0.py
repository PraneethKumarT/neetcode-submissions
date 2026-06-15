class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]
        area = 0

        while l < r:
            if height[l] <= height[r]:
                area += max(0, maxL - height[l])
                maxL = max(height[l], maxL)
                l += 1
            else:
                area += max(0, maxR - height[r])
                maxR = max(height[r], maxR)
                r -= 1

        return area    
        

            
            