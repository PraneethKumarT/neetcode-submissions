class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r= 0, len(numbers)-1

        while l<r:
            lnum = numbers[l]
            rnum = numbers[r]

            if lnum + rnum == target:
                return [l+1, r+1]
            elif lnum+rnum < target:
                l += 1
            else:
                r -= 1
            
        