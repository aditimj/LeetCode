class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a','A','e','E','i','I','o','O','u','U']
        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and s[left] not in vowel:
                left += 1

            while left < right and s[right] not in vowel:
                right -= 1
            if left < right:
                s[right], s[left] = s[left],s[right]
                left +=1
                right -= 1
        return ''.join(s)
        



        