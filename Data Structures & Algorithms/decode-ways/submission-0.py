class Solution:
    def numDecodings(self, s: str) -> int:

        stack = ""
        cache = {}
        def helper(i):

            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            if i in cache:
                return cache[i]
            
            count = helper(i+1)

            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                count += helper(i+2)

            cache[i] = count
            return count
        
        return helper(0)
"""
12236
"""
            
            
        


"""
cannot start with a 0
single digit or double digit

"""