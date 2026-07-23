class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        data_mapping = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        data = []
        for digit in digits:
            data.append(data_mapping[digit])
        
        res = []
        stack = []

        def helper(i):
            if len(stack) == len(digits):
                res.append(''.join(stack))
                return
            
            for char in data[i]:
                stack.append(char)
                helper(i+1)
                stack.pop()
        
        helper(0)
        return res

                



        
        

"""

234
abc, def, ghi

for each of the string:
    include char
    Not include char


"""