class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        cnt1 = {}
        cnt2 = {}
        res = []
        for i in nums1:
            if i in cnt1:
                cnt1[i] += 1
            else:
                cnt1[i] = 1
        for i in nums2:
            if i in cnt2:
                cnt2[i] += 1
            else:
                cnt2[i] = 1
        print(cnt1)
        print(cnt2)
        for key in cnt1:
            if key in cnt2:
                count = min(cnt1[key],cnt2[key])
                res.extend([key] * count)
        return res







        