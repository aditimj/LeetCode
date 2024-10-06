class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(0,len(operations)):
            try:
                num = int(operations[i])
                stack.append(num)
            except:
                if operations[i] == \D\:
                    if stack:
                        stack.append(stack[-1]*2)
                if operations[i] == 'C':
                    if stack:
                        stack.pop()
                if operations[i] == '+':
                    if stack:
                        stack.append(stack[-1] + stack[-2]) 
        if stack:
            return sum(stack)
        return 0

                



        