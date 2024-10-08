class Solution:
    def minSwaps(self, s: str) -> int:
        imb = 0
        maximb = 0
        for i in s:
            if i == '[':
                imb -= 1
            else:
                imb += 1
            maximb = max(maximb,imb)
        return (maximb + 1) // 2



