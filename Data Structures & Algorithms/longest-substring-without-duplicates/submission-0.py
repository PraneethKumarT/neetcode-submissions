class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        L = 0
        maxSize = 0

        for R in range(len(s)):
            char = s[R]

            while char in window:
                window.remove(s[L])
                L += 1

            window.add(char)
            maxSize = max(maxSize, R-L + 1)
            
        return maxSize