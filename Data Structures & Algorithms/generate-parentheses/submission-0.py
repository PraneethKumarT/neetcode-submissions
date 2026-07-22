class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def helper(current, openCnt, closeCnt):

            if openCnt == closeCnt == n:
                res.append(current)
                return
            
            if openCnt < n:
                helper(current + "(", openCnt+1, closeCnt)
            
            if closeCnt < openCnt:
                helper(current + ")", openCnt, closeCnt+1)
            
        helper("", 0 , 0)
        return res
            



        
        

"""
( ( ( ) ) )

())

"""