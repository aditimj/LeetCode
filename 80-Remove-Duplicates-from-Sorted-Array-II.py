class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        start_ind = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[start_ind - 2]:
                nums[start_ind] = nums[i]
                start_ind += 1
        return start_ind
        