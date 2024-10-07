class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        ans = ""
        diff = 0
        for i,j in zip(word1,word2):
            ans += i
            ans += j
        if len(word1) > len(word2):
            diff = len(word1) - len(word2)
            ans = concat(ans , word1[-diff:])
        if len(word2) > len(word1):
            diff = len(word2) - len(word1)
            ans = concat(ans , word2[-diff:])
        return ans
        