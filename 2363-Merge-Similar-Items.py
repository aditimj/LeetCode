class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        item_map = {}

        for v, w in items1:
            if v in item_map:
                item_map[v] += w 
            else:
                item_map[v] = w 

        for v, w in items2:
            if v in item_map:
                item_map[v] += w 
            else:
                item_map[v] = w  

        ans = sorted(item_map.items())  

        return ans

        