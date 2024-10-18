class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        ans = []
        cntmap = {}
        for i in range(len(nums) - k + 1):
            for j in range(i,i+k):
                if nums[j] in cntmap:
                    cntmap[nums[j]] += 1
                else:
                    cntmap[nums[j]] = 1
            for key,val in cntmap.items():
                sorted_items = sorted(cntmap.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
                top_x_items = sorted_items[:x]
                total_sum = 0
                for key, value in top_x_items:
                    total_sum += int(key) * value
            ans.append(total_sum)
            cntmap.clear()
        return ans



        