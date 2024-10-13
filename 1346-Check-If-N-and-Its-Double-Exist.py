class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        val = 0
        for i in range(0,len(arr)):
            val = arr[i] * 2
            if val in arr and arr.index(val) != i:
                return True
        return False
        