import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', \\, s)
        t = s[::-1]
        ans = s==t
        return ans
        