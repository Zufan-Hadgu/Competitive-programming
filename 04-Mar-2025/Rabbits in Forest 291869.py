# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

 

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = Counter(answers)
        output = 0
        
        for ans in d:
            while d[ans] > ans:
                output += (ans + 1)
                d[ans] -= (ans + 1)

            if d[ans] > 0:
                output += (ans + 1)
        
        return output
