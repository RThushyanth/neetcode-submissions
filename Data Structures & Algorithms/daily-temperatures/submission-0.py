class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        answers = [0]*len(temperatures)
        for i in range(1,len(temperatures)):
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while temperatures[stack[-1]] < temperatures[i]:
                    answers[stack[-1]] = i - stack[-1]
                    stack.pop()
                    if len(stack) == 0:
                        break
                stack.append(i)


        return answers