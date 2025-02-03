# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
            
        lost = {}  
        answer1 = []  
        answer0 = set()   

         
        for i in range(len(matches)):
            if matches[i][1] in lost:
                lost[matches[i][1]] += 1
            else:
                lost[matches[i][1]] = 1

       
        for i in range(len(matches)):
            if lost.get(matches[i][1], 0) == 1:   
                answer1.append(matches[i][1])
            
            if matches[i][0] not in lost:  
                answer0.add(matches[i][0])

        answer0 = sorted(answer0) 
        answer1.sort()

        return [answer0, answer1]

            