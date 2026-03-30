class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t != '+' and t != '-' and t != '/' and t != '*':
                stack.append(int(t))
            else:
                num2  = stack.pop()
                num1 = stack.pop()
                if t == '+':
                    stack.append(num1 + num2)
                elif t == '-':
                    stack.append(num1 - num2)
                elif t == '*':
                    stack.append(num1 * num2)
                elif t == '/':
                    stack.append( int(num1 / num2))
        return stack.pop()

        

