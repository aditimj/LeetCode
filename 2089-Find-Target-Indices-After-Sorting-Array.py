class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        nums = sorted(nums)
        ans = []
        for i in range(0,len(nums)):
            if nums[i] == target:
                ans.append(i)
            if nums[i] > target:
                break
        return ans

        