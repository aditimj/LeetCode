class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum1 = n * (n+1)//2
        sum2 = sum(nums)
        num1 = 0
        addnum = set()
        arr = []
        for i in nums:
            if i in addnum:
                num1 = i
                arr.append(num1)
                break
            else:
                addnum.add(i)        
        diff = sum1 - sum2
        num2 = num1 + diff
        arr.append(num2)
        return arr



        