class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2 != 0:
            return False

        stack = []
        
        for i in range(0,len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False

                elif stack[-1] == "(" and s[i] == ")":
                    stack.pop()

                elif stack[-1] == "[" and s[i] == "]":
                    stack.pop()

                elif stack[-1] == "{" and s[i] == "}":
                    stack.pop()
                
                else:
                    return False
        
        if len(stack) !=0:
            return False
        else:
            return True
            
