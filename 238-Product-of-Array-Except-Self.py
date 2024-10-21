import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
        prod = math.prod(nums)
        ans = []
        ind = []
        new = set(nums)
        if len(new) == 1 and 0 in new:
            return nums
        for i in range(0,len(nums)):
            if nums[i] == 0:
                nums[i] = 1
                ind.append(i)
        if len(ind) > 1:
            return([0] * len(nums))
        prod_0 = math.prod(nums)
        for i in range(0,len(nums)):
            if prod == 0 and i in ind:
                ans.append(prod_0)
            elif prod == 0 and i not in ind:
                ans.append(0)
            else:
                ans.append(prod//nums[i])
        return ans

        