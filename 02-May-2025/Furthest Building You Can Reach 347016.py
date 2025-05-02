# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # l = 0
        # r = 1
        # needed_briecks = 0
        # while l < r and r < len(heights):
        #     if heights[r] > heights[l]:
            
        #         needed_briecks = heights[r] - heights[l]
        #         if needed_briecks <= bricks:
        #             bricks = bricks - needed_briecks
        #         elif needed_briecks > bricks and ladders != 0:
        #             ladders -= 1
        #         else:
        #             return l
        #     r += 1
        #     l += 1
        # return l

        min_heap = []
        l = 0
        r = 1
        while l < r and r< len(heights):
            jump = heights[r] - heights[l]
            if jump > 0:
                heapq.heappush(min_heap,jump)
            if len(min_heap)> ladders:
                bricks -= heapq.heappop(min_heap)
            if bricks < 0:
                return l
            r += 1
            l += 1
        return l




        