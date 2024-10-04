class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {')': '(', '}': '{', ']':'[' }
        if len(s) > 1:
            for i in s:
                if i in pairs.values():
                    stack.append(i)
                elif i in pairs.keys():
                    if stack and stack[-1] == pairs[i]:
                        stack.pop()
                    else: 
                        return False
        else:
            return False
        return len(stack) == 0

        





        # stack = []
        # pairs = {')': '(', '}': '{', ']': '['}  
        
        # for char in s:
        #     if char in pairs.values():  
        #         stack.append(char)
        #     elif char in pairs.keys(): 
        #         if not stack or stack[-1] != pairs[char]:  
        #             return False
        #         stack.pop()  
        
        # return len(stack) == 0  