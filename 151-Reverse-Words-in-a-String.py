class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ans = []
        for i in range(len(s)-1,-1,-1):
            ans.append(s[i])
        s = ' '.join(ans)
        return s

        