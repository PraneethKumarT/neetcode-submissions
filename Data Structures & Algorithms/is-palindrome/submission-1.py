class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not str.isalnum(s[left]):
                left += 1

            while left < right and not str.isalnum(s[right]):
                right -= 1      

            if s[left].lower() == s[right].lower():
                left = left+1
                right = right-1
            else:
                return False
            
        return True
        