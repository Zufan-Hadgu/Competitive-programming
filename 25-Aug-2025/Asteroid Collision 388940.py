# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            current = asteroids[i]
            while stack and stack[-1] > 0 and current < 0:
                top = stack[-1]
                if abs(top) < abs(current):
                    stack.pop()
                    continue
                elif abs(top) == abs(current):
                    stack.pop()
                break
            else:
                stack.append(current)
        
        return stack