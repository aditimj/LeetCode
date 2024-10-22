class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        x = list(x)
        ans = []
        for i in range(len(x)-1,-1,-1):
            ans.append(x[i])
        if ans[-1] == '-':
            ans.insert(0,'-')
            del ans[-1]
        x = ''.join(ans)
        x = int(x)
        if x < -2**31 or x > (2**31 -1):
            return 0
        return x

        

        