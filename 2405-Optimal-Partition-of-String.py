class Solution:
    def partitionString(self, s: str) -> int:

        seen = set()
        cnt = 1
        for i in s:
            if i in seen:
                cnt +=1
                seen.clear()
            seen.add(i)
        return cnt




        