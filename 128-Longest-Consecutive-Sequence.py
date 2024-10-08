class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        seen = set()
        ans = []
        if len(nums) == 0:
            return 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                seen.add(nums[i])
            if nums[i+1]  - nums[i] > 1:
                ans.append(len(seen) +1)
                seen.clear()

        ans.append(len(seen) +1)

        return max(ans)





        