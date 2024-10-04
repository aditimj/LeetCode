class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        ans = []
        pos = sorted(score, reverse = True)
        mydict = {}
        if len(pos) > 0:
            mydict[pos[0]] = 'Gold Medal'
        if len(pos) > 1:
            mydict[pos[1]] = 'Silver Medal'
        if len(pos) > 2:
            mydict[pos[2]] = 'Bronze Medal'
        for i in range(3,len(pos)):
            mydict[pos[i]] = str(i+1)
        for i in score:
            val = mydict[i]
            ans.append(val)
        return ans





        