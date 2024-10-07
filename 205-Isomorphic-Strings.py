class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        if len(s) != len(t):
            return False
        for i, j in zip(s,t):
            if i in smap:
                if smap[i] != j:
                    return False
            else:
                smap[i] = j
            if j in tmap:
                if tmap[j] != i:
                    return False
            else:
                tmap[j] = i
        return True
