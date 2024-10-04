class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        ctype = set(candyType)
        allowed = len(candyType)//2
        ans = 0
        if len(ctype) < allowed:
            ans = len(ctype)
        elif len(ctype) > allowed:
            ans = allowed
        else:
            ans = allowed
        return ans
        