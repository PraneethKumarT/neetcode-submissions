class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charMap = {}
        maxLen, maxFreq, l = 0, 0, 0

        for r, ch in enumerate(s):
            charMap[ch] = 1 + charMap.get(ch, 0)

            maxFreq = max(maxFreq, charMap[ch])

            while (r-l+1) - maxFreq > k:
                charMap[s[l]] -= 1
                l+=1
            
            maxLen = max(maxLen, r-l+1)
        
        return maxLen

           
        