class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = {}
        first = {}
        last = {}
        
        # Traverse through the array to fill the dictionaries
        for i, num in enumerate(nums):
            if num not in freq:
                freq[num] = 0
                first[num] = i  # record the first occurrence of num
            freq[num] += 1
            last[num] = i  # update the last occurrence of num

        # Find the degree of the array
        degree = max(freq.values())
        
        # Find the minimum length of subarray that has the same degree
        min_length = len(nums)
        for num in freq:
            if freq[num] == degree:
                min_length = min(min_length, last[num] - first[num] + 1)
        
        return min_length