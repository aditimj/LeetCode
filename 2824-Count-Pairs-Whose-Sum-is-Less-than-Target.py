class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        cnt = 0
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] < target:
                cnt += (j-i)
                i +=1
            else:
                j -= 1
        return cnt
            




        # i = 0
        # j = 1        
        # while i < j and j < len(nums):
        #     print(i,j,nums[i] + nums[j])
        #     if nums[i] + nums[j] < target:
        #         cnt += 1
        #         j += 1
        #         if j == len(nums) - 1 and i != len(nums) - 2:
        #             if nums[i] + nums[j] < target:
        #                 cnt += 1
        #                 i += 1
        #                 j = i + 1
        #     else: 
        #         i += 1
        #         j = i + 1
        # return cnt

            


        