class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        nums = reversed(sorted(nums))
        ans = []
        for num in nums:
            if num > 0:
                seen.add(num)
            elif num < 0 and abs(num) in seen:
                ans.append(abs(num))
        if not ans:
            return -1
        return max(ans)
        