class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        map1 = {}
        map2 = {}
        pnt1 = 0
        pnt2 = 0
        map3 = {}
        for i in list1:
            map1[i] = pnt1
            pnt1 +=1
        for j in list2:
            map2[j] = pnt2
            pnt2 +=1    
        for key in map1:
            if key in map2:
                map3[key] = map1[key] + map2[key]
        ans = []
        if map3:
            min_key = min(map3.values())
            for key,values in map3.items():
                if values == min_key:
                    ans.append(key)
        return ans
        

