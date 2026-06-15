class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        results = [0] * len(temperatures)
        stk = []

        for i in range(0, len(temperatures)):
            while len(stk)> 0 and temperatures[stk[-1]] < temperatures[i]:
                    print(stk, " i " , str(i) , " temp " , temperatures[i])
                    popped = stk.pop()
                    results[popped] = i - popped    
            stk.append(i)
        
        return results
    
    
    """
        [30,38,30,36,35,40,28]
        [1,4,1,2,1,0,0]

        stk = [38,36,]



        28 40 35 36 30 38 30


    """