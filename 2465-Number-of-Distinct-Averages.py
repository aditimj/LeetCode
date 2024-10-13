class Solution:
    def distinctAverages(self, nums: List[int]) -> int:

        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        res = set()
        while left < right:
            avg = (nums[left] + nums[right]) / 2
            if avg not in res:
                res.add(avg)
            avg = 0
            left += 1
            right -= 1
        return len(res)
        