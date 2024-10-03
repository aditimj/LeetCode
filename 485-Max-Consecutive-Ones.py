class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        ans = []

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            if nums[i] != 1:
                cnt = 0
            print(cnt)
            ans.append(cnt)
        ans = sorted(ans)
        print(ans)
        return ans[-1]
        