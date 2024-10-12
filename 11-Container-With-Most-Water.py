class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        width = 0
        max_area = 0
        while left < right:
            width = right - left
            vol = min(height[left], height[right]) * width
            max_area = max(vol,max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

#brute force

        # ans = [0]
        # for i in range(0, len(height)):
        #     for j in range(len(height)-1,-1,-1):
        #         if height[i] < height[j]:
        #             vol = height[i] * (j-i)
        #             if ans:
        #                 if vol > ans[-1]:
        #                     ans.append(vol)
        #                     vol = 0
        #         else:
        #             vol = height[j] * (j-i)
        #             if ans:
        #                 if vol > ans[-1]:
        #                     ans.append(vol)
        #                     vol = 0
        # return max(ans)
        