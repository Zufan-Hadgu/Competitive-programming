# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        result = []
        for i in range(len(s)):
            d[s[i]] += 1
        print(d)
        freq = []
        for values in d.values():
             freq.append(values)
        freq.sort(reverse=True)

        processed = set()
        for i in range(len(freq)):
            for key,values in d.items():
                if values == freq[i] and key not in processed:
                    result.append(key*freq[i])
                    processed.add(key)
        return "".join(result)

 

        

        