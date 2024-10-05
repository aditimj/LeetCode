class Solution:
    def firstUniqChar(self, s: str) -> int:
        mydict = {}
        ans = 0
        for i in s:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        for key,val in mydict.items():
            if val == 1:
                ans = key
                break
        if ans:
            ind = s.index(ans)
        else:
            return -1
        return ind
        