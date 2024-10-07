class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mydict = {}
        for i in nums:
            if i in mydict:
                mydict[i] +=1
            else:
                mydict[i] = 1
        ans = []
        for keys, val in mydict.items():
            if val > len(nums)/3:
                ans.append(keys)
        return ans
        