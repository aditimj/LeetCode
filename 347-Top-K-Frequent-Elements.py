class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        def get_value(item):
            return item[1]
        new = dict(sorted(freq.items(), key=get_value, reverse=True))
        out = dict(itertools.islice(new.items(),k))
        ans = []
        for key in out.keys():
            ans.append(key)
        return ans
        