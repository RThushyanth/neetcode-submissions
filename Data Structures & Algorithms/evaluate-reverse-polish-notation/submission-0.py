class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(0,len(tokens)):
            if tokens[i] != '+' and tokens[i] != '-' and tokens[i] !='*' and tokens[i] != '/':
                stack.append(tokens[i])
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if tokens[i] == "+":
                    stack.append(a+b)
                elif tokens[i] == "-":
                    stack.append(b-a)
                elif tokens[i] == "*":
                    stack.append(a*b)
                elif tokens[i] == "/":
                    if not (a <0 and b < 0) and (a < 0 or b <0):
                        stack.append(-(abs(b)//abs(a)))
                    else:
                        stack.append(b//a)
        
        return int(stack[0])