class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            # print('i',i)
            # print(f'res {res} ^ i {i}')
            res ^= i
            # print('res',res)
        return res   