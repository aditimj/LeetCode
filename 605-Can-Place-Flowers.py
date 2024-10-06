class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:        
        cnt = 0   
        if len(flowerbed) > 2: 
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                cnt += 1
                flowerbed[0] = 1
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                cnt+= 1
                flowerbed[-1] = 1
        if flowerbed[0] == 0 and len(flowerbed) ==1:
            cnt = 1
        if flowerbed[0] == 1 and len(flowerbed) ==1:
            cnt = 0
        if cnt>=n:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if (flowerbed[i - 1] == 0) and (flowerbed[i + 1] == 0):
                    flowerbed[i] = 1  
                    cnt += 1  
                    if cnt >= n:
                        return True
        return cnt >= n
            