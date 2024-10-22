class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num = list(str(num))
        if len(num)==1:
            return True
        if num[-1] == str(0):
            print('here')
            return False
        else:
            return True

        