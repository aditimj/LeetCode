class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        arr = sorted(nums)
        sum = 0
        for i in range(0,len(arr),2):
            sum = sum + arr[i]
        return sum

        