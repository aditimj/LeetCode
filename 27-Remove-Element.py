class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = []
        for i in range(len(nums)):
            if nums[i] != val:
                ans.append(nums[i])
        for i in range(len(ans)):
            nums[i] = ans[i]
        return len(ans)


        