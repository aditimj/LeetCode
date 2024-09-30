class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cnt = {}
        for i in range(len(nums)):
            if nums[i] in cnt:
                if abs(i - cnt[nums[i]]) <= k:
                    return 1
            cnt[nums[i]] = i
        return 0

        # cnt= 0
        # tmp = 0
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j] and abs(i-j) <=k:
        #             cnt +=1
        #             print(i,j,cnt)
        #         if nums[i] == nums[j] and abs(i-j) > k:
        #             tmp = +1
        # if tmp > 0 and cnt == 0:
        #     return False
        # if cnt > 0:
        #     return True
        # return False

        