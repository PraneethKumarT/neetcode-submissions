class Solution:
    def minWindow(self, s: str, t: str) -> str:

        needMap = Counter(t)
        windowMap = {}
        need, have, L = len(needMap), 0, 0
        res, resLen = [-1, -1], float("infinity")

        for i, ch in enumerate(s):

            windowMap[ch] = windowMap.get(ch,0)+1

            if ch in t and windowMap[ch] == needMap[ch]:
                have += 1

            while need == have:
                if(i-L+1) < resLen:
                    res = [L, i]
                    resLen = min(resLen, i-L+1)
                
                windowMap[s[L]] -= 1
                if s[L] in t and windowMap[s[L]] < needMap[s[L]]:
                    have -= 1
                L+=1

        L, i = res
        return s[L:i+1]



            

"""
case 1: Perfect
    s = "ABCD" t = "BCD"

case 2: Optimal
    s = "ABZBABCD" t = ABCD

"""
        