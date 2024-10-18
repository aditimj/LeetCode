class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sneaky_num = set()
        ans = []

        for i in nums:
            if i in sneaky_num:
                ans.append(i)
            else:
                sneaky_num.add(i)
        return ans

        