from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        
        cnt = {}      
        for i, num in enumerate(nums_sorted):
            if num not in cnt:
                cnt[num] = i
        ans = []
        for num in nums:
            ans.append(cnt[num])        
        return ans
