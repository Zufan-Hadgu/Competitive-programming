# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        result = []
        for s in strs:
            word = sorted(s)
            word = "".join(word)
            d[word].append(s)
        for anagram in d.values():
            result.append(anagram)
        return(result)

            

       



        