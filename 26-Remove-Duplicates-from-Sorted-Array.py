class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = list(dict.fromkeys(nums))
        for i in range(len(ans)):
            nums[i]= ans[i]
        return len(ans)


        