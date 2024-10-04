class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.strip()
        string = string.split()
        string = string[-1]
        ans = len(string)
        return ans

        