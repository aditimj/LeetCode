class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        if target > nums[-1]:
            return len(nums)
        else:
            for i in range(len(nums)):
                if nums[i] >= target:
                    return i

        