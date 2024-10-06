class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mydict = {
            'a': ".-",'b': "-...",'c': "-.-.",
            'd': "-..",
            'e': ".",
            'f': "..-.",
            'g': "--.",
            'h': "....",
            'i': "..",
            'j': ".---",
            'k': "-.-",
            'l': ".-..",
            'm': "--",
            'n': "-.",
            'o': "---",
            'p': ".--.",
            'q': "--.-",
            'r': ".-.",
            's': "...",
            't': "-",
            'u': "..-",
            'v': "...-",
            'w': ".--",
            'x': "-..-",
            'y': "-.--",
            'z': "--.."
        }
        ans = []
        for word in words:
            result = ""
            for char in word:
                if char in mydict:
                    result += mydict[char]
            ans.append(result)
        res = len(set(ans))
        return res
        