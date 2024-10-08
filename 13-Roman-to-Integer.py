class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {\I\: 1, \V\:5, \X\:10, \L\:50, \C\:100, \D\:500, \M\:1000}
        num = 0
        for i in range(0,len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                num -= roman[s[i]]
            else:
                num += roman[s[i]]
        return num
        