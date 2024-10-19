class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        flag = False
        largestnum = max(nums)
        for i in range(len(nums)):
            if largestnum >= 2 * nums[i] or largestnum == nums[i]:
                flag = True
            else:
                return -1
        if flag == True:
            index = nums.index(largestnum)
            return index
        

        