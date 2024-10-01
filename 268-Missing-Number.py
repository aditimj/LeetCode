
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        tot = (n * (n + 1))//2
        act = sum(nums)
        ans = tot - act
        return ans


        # mylist = []
        # mylist = sorted(nums)
        # ans = 0
        # if len(mylist)==1 and mylist[0] != 0:
        #     ans = mylist[0] - 1
        #     return ans
        # if len(mylist)==1:
        #     ans = mylist[0] + 1
        #     return ans
        # for i in range(len(mylist)-1):
        #     if mylist[i+1] - mylist[i] > 1:
        #         ans = mylist[i+1] - 1
        #     else:
        #         ans = mylist[i+1] + 1
            
        # return ans
        