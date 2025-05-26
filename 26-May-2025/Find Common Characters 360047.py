# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d = Counter(words[0])
        output = []

        for word in words[1:]:
            temp = Counter(word)
            for letter in list(d.keys()):   
                if letter not in temp:
                    del d[letter]
                else:   
                    d[letter] = min(d[letter], temp[letter])   

        for letter in d:
            output.extend([letter] * d[letter])   

        return output