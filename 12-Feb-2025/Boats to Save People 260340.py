# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        output = 0
        people.sort()
        l = 0
        r = len(people) -1
         
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            output += 1
            r -= 1
        return output 

            


        