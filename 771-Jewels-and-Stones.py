class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jset = set(jewels)
        cnt = 0
        for i in stones:
            if i in jset:
                cnt += 1
        return cnt



        # jmap = {}
        # smap = {}
        # for i in stones:
        #     if i in smap:
        #         smap[i] +=1
        #     else:
        #         smap[i] = 1
        # for i in jewels:
        #     if i in jmap:
        #         jmap[i] +=1
        #     else:
        #         jmap[i] = 1
        # common = set(smap.keys()).intersection(jmap.keys())
        # sum = 0
        # for key in common:
        #     sum += smap[key]
        # return sum

        