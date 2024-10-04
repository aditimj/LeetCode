class Solution:\r
    def findLHS(self, nums: List[int]) -> int:\r
        arr = sorted(nums)\r
        mydict = {}\r
        for i in arr:\r
            if i in mydict:\r
                mydict[i] +=1\r
            else:\r
                mydict[i]  = 1\r
        sorted_keys = sorted(mydict.keys())\r
        max_sum = 0\r
        for i in range(1, len(sorted_keys)):\r
            if sorted_keys[i] - sorted_keys[i-1] == 1: \r
                valsum = mydict[sorted_keys[i]] + mydict[sorted_keys[i-1]]\r
                max_sum = max(max_sum,valsum)\r
        return max_sum\r
\r
\r
