class Solution:
    def maximumProduct(self, nums: List[int]) -> int:            
        
        nums = sorted(nums,reverse = True)
        return max((nums[-1] * nums[-2] * nums[0]), (nums[0] * nums[1]* nums[2]))