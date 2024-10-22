class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        currsum =  sum(nums[:k])
        maxsum = currsum
        for i in range(k, len(nums)):
            currsum += nums[i] - nums[i-k]
            maxsum = max(maxsum,currsum)
        return maxsum/k




        # avg = float('-inf')
        # sum1 = 0
        # x = k
        # if len(nums) == 1 and k == 1:
        #     return nums[0]/k
        # for i in range(0,len(nums)-k+1,1):
        #     sum1 = sum(nums[i:x])
        #     avg = max(avg, sum1/k)
        #     x += 1
        # return avg


