class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # int() truncates division toward zero, which handles negatives correctly
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        
        return stack[0]

"""
["1","2","+","3","*","4","-"]
[-, 4, *, 3, +, 2, 1]

"""