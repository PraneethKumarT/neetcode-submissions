class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}
        def helper(amt):
            if amt == 0:
                return 0

            if amt in cache:
                return cache[amt] 
            
            min_req = 999
            
            for coin in coins:
                if amt-coin >= 0:
                    res = min(min_req,helper(amt-coin))
                    if res != 999:
                        min_req = min(min_req, 1+res)
                
            cache[amt] = min_req
            return min_req
        
        ans = helper(amount) 
        if ans == 999:
            return -1
        else:
            return ans
         
        


"""
[1,5,10]
amt = 12

        10
    1 5  10
 1

        5
    1   5   10
 1  5   1 
1 5  1.  1

            12
   11.          7.          2
 10  6  1     6   2      1. 
            1  5          1
                0

when rem is in coin -> return
when cache[i] where i is remaininh -> return           
"""