# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()
        l = 0
        r = 0
        output = 0
        for i in range(len(students)):
            output += abs(students[r] - seats[l])
            r += 1
            l += 1
        return output 


        