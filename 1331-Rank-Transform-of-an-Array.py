class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranked = sorted(arr)    
        rmap = {}
        cnt = 0
        ans = []
        for i in ranked:
            if i in rmap:
                rmap[i] == rmap[i]
            else:
                rmap[i] = 1 + cnt
                cnt += 1            
        for i in arr:
            if i in rmap:
                ans.append(rmap[i])
        return ans



        