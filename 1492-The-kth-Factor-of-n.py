class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        kfac = {}
        cnt = 1
        for i in range(1,n+1):
            if n % i == 0:
                kfac[i] = cnt
                cnt +=1
        print(kfac)
        if k in kfac.values():
            for key, values in kfac.items():
                if values == k:
                    return key

        return -1


        