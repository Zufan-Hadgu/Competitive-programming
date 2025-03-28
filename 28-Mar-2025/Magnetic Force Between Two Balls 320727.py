# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 1
        right = position[-1] - position[0]
        ans = 0
        def valid(mid):
            pos = position[0]
            balls = 1
           
            for i in range(1,len(position)):
                if abs(position[i] - pos)>= mid:
                    balls += 1
                    pos = position[i]    
            return balls >= m

        while left <= right:
            mid = (left+right)//2
            if valid(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1 
        return ans



        