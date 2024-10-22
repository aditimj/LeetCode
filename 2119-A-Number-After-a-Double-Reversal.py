class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        rev1 = 0
        rev2 = 0
        num1 = str(num)
        num1 = list(num1)
        ans = []
        ans2 = []
        for i in range(len(num1)-1,-1,-1):
            ans.append(num1[i])
        rev1 = ''.join(ans)
        rev1 = int(rev1)  
        num2 = str(rev1)
        num2 = list(num2)
        for i in range(len(num2)-1,-1,-1):
            ans2.append(num2[i])
        rev2 = ''.join(ans2)
        rev2 = int(rev2)        
        return num == rev2

        