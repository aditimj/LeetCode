class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rmap = {}
        mmap = {}
        for i in ransomNote:
            if i in rmap:
                rmap[i] += 1
            else:
                rmap[i] = 1
        for i in magazine:
            if i in mmap:
                mmap[i] += 1
            else:
                mmap[i] = 1
        for i in rmap:
            if rmap[i] > mmap.get(i,0):
                return False
        return True

        