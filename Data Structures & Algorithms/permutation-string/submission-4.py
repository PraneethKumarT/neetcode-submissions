class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        charMap = Counter(s1)
        L = 0
        for i,ch in enumerate(s2):
            
            if len(charMap) == 0:
                return True

            if ch in charMap:
                charMap[ch] = charMap.get(ch) - 1
                if charMap[ch] == 0:
                    del charMap[ch]
            else:
                while L <= i:
                    if s2[L] in s1:
                        charMap[s2[L]] = charMap.get(s2[L], 0) + 1
                    
                    L += 1
                    if ch in charMap:
                        charMap[ch] -= 1
                        if charMap[ch] == 0:
                            del charMap[ch]
                        break

        return len(charMap) == 0             