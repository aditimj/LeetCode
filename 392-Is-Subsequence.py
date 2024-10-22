class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0
        j = 0
        cnt = 0
        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                cnt += 1
                j +=1
                i+=1
            else:
                j +=1
        if cnt == len(s):
            return True
        return False

        