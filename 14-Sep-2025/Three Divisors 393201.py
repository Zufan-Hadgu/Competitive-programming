# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        if n <= 3:
            return False

        output = []
        for i in range(1, n + 1):   
            if n % i == 0:          
                output.append(i)

        return len(output) == 3