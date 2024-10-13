class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        ans = []
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            avg = (nums[left] + nums[right]) / 2
            ans.append(avg)
            left += 1
            right -= 1
        return min(ans)


        