class Solution:
    def compress(self, chars: List[str]) -> int:

        s = []
        cnt = 0
        for i in range(0,len(chars)):
            if i == 0:
                s.append(chars[i])
                cnt += 1
            elif chars[i] == chars[i-1]:
                cnt+=1
            else:
                if cnt == 1:
                    s.append(chars[i])
                    cnt = 1
                else:
                    s.append(str(cnt))
                    s.append(chars[i])
                    cnt = 1
        if cnt != 1:
            s.append(str(cnt))
        s = ''.join(s)
        s = list(s)
        chars[:len(s)] = s
        chars[:] = chars[:len(s)]
        return len(chars)





        # smap ={}
        # for i in chars:
        #     if i in smap:
        #         smap[i] +=1
        #     else:
        #         smap[i] = 1
        # ind = 0
        # for key, value in smap.items():
        #     chars[ind] = key
        #     ind +=1
        #     if value > 1:
        #         for digit in str(value):
        #             chars[ind] = digit
        #             ind += 1
 
        # return ind

        