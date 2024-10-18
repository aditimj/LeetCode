class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for word in strs:

            sorted_word = ''.join(sorted(word))
            res[sorted_word].append(word)
        ans = []
        for values in res.values():
            ans.append(values)

        return ans

        
            



        