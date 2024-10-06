class Solution:
    def maximumProduct(self, nums: List[int]) -> int:            
        
        nums = sorted(nums,reverse = True)
        prod = 0
        if nums[-1] * nums[-2] * nums[0] > nums[0] * nums[1] * nums[2]:
            prod = nums[-1] * nums[-2] * nums[0]  
        else:
            prod = nums[0] * nums[1] * nums[2]  
        return prod