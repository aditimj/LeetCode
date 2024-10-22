class Solution:
    def isHappy(self, n: int) -> bool:
        arr = []
        while True:
            sum1 = 0
            while n > 0:
                rem = n % 10
                sum1 += (rem**2)
                n = n//10
            if sum1 == 1:
                return True
            if sum1 in arr:
                return False
            arr.append(sum1)
            n = sum1
        return 0





        # digits = []
        # def spl(n):
        #     while n > 0:
        #         digits.insert(0,n%10)
        #         n //= 10
        #     return digits
        # sum1 = 0
        # while sum1  != 1 or len(digits) != 1:
        #     spl(n)
        #     sum1 = sum(x**2 for x in digits)
        # if sum1 == 1:
        #     return True
        


        