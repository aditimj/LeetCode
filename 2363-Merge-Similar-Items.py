class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        item1map = {}
        item2map = {}
        for v, w in items1:
            item1map[v] = w
        for v, w in items2:
            item2map[v] = w
        sitem2map = dict(sorted(item2map.items(), key = lambda item:item[0]))
        sitem1map = dict(sorted(item1map.items(), key = lambda item:item[0]))
        ans = []
        for key, val in sitem1map.items():
            if key in sitem2map:
                ans.append([key, sitem1map[key] + sitem2map[key]])
            else:
                ans.append([key,sitem1map[key]])
        for key, val in sitem2map.items():
            if key not in sitem1map:
                ans.append([key, val])
        ans.sort(key=lambda item: item[0])
        return ans

        