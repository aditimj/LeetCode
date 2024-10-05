class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        mydict = {}
        mydict2 = {}
        pattern = list(pattern)
        s = s.split()
        if len(s) != len(pattern):
            return False
        for i,word in zip(pattern,s):
            if i in mydict:
                if mydict[i] != word:
                    return False
            else:
                mydict[i] = word
            if word in mydict2:
                if mydict2[word] != i:
                    return False
            else:
                mydict2[word] = i
        return True       