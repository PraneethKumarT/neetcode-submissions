class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        stack = []
        def helper(openCnt, closeCnt):

            if openCnt == closeCnt == n:
                res.append("".join(stack))
                return
            
            if openCnt < n:
                stack.append("(")
                helper(openCnt+1, closeCnt)
                stack.pop()
                
            
            if closeCnt < openCnt:
                stack.append(")")
                helper(openCnt, closeCnt+1)
                stack.pop()
                
            
        helper(0 , 0)
        return res
            



        
        

"""
( ( ( ) ) )

())

"""