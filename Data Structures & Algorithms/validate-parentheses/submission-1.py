class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        close_to_open = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        for ch in s:
            if ch in close_to_open:
                if not stk or stk[-1] != close_to_open[ch]:
                    return False
                stk.pop()
            else:
                stk.append(ch)
        
    
        return len(stk) == 0
        