class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        ans = []
        n = max(candies)
        for i in range(0,len(candies)):
            if candies[i] +  extraCandies >= n:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        