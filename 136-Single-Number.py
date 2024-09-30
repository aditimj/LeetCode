class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        cnt = {}
        ans = 0
        for i in nums:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i]=1
        for key,values in cnt.items():
            if values == 1:
                ans = key
        return ans
        



        # res = 0
        # for i in nums:
        #     res ^= i
        # return res   