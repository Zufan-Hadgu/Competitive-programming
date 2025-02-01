# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pillow = 1
        step = 1
        for i in range(time):
            pillow += step

            if pillow == n or pillow == 1:
                step *= -1
        return pillow 
     