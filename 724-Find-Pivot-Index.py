class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        tot = sum(nums)
        left_sum = 0
        for i in range(0,len(nums)):

            if left_sum == tot - left_sum - nums[i]:
                return i
            left_sum = left_sum + nums[i]
    
        return -1

        