class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # ans = []
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i]==nums2[j] and nums1[i] not in ans:
        #             ans.append(nums1[i])
        # return ans

        ans = set()
        for num in nums1:
            if num in nums2:
                ans.add(num)
        return ans
                    
        