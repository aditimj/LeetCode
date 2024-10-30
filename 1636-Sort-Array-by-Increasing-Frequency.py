class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = {}
        for i in nums:
            if i in cnt:
                cnt[i] +=1
            else:
                cnt[i] = 1
        sorted_data_desc = dict(sorted(cnt.items(), key=lambda item: (item[1], -item[0])))
        ans = []
        for key, val in sorted_data_desc.items():
            for _ in range(val):  # Repeat the key 'val' times
                ans.append(key)  
        return ans
        