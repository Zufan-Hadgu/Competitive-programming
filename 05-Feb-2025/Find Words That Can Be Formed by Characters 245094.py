# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_d = defaultdict(int)
        for char in chars:
            chars_d[char] += 1
        print(chars_d)    
        result = []

        for word in words:
            word_d = defaultdict(int)
            for car in word:
                word_d[car] += 1       
            valid = True
            for key,values in word_d.items():
                if values > chars_d.get(key,0):
                    valid = False
                    break
            if valid:
                result.append(word)
            
        _sum = 0
        for good in result:
            _sum += len(good)

        return (_sum)
            
 