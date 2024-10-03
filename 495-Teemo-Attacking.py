class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:   
        tot = 0
        for i in range(len(timeSeries)-1):            
            tot += min(timeSeries[i+1] - timeSeries[i],duration)
          
        tot += duration
        return tot
        
        # tot = 0
        # ans = []
        # add = 0
        # for i in timeSeries:
        #     num1 = i
        #     num2 = i + duration - 1
        #     for i in range(num1, num2 +1):
        #         ans.append(i)
        # res = set(ans)
        # final = len(res)
        # return final
