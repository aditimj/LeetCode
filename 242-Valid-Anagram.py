class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps = {}
        mapt = {}
        for i in s:
            if i in maps:
                maps[i] += 1
            else:
                maps[i] = 1
        for i in t:
            if i in mapt:
                mapt[i] += 1
            else:
                mapt[i] = 1
        is_equal = Counter(maps) == Counter(mapt)
        return is_equal


        