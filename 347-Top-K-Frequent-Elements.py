class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        new = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        out = dict(itertools.islice(new.items(),k))
        ans = []
        for key in out.keys():
            ans.append(key)
        return ans
        