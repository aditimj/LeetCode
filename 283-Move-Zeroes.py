class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cnt] = nums[i]
                cnt += 1
        for i in range(cnt, len(nums)):
            nums[i] = 0
      
        
        
        



        
            
        