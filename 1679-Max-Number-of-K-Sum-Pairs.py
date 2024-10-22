class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        cnt = 0
        while i < j and j < len(nums):
            if nums[i] + nums[j] == k:
                cnt += 1
                i += 1
                j -=1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1            
        return cnt



        