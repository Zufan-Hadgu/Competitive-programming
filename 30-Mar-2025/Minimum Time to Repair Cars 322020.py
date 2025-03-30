# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        right = max(ranks)*cars*cars
        left = 1
        ans = 0
        def repair(time):
            
            total_car = 0
            for rank in ranks:
                total_car += int((time // rank) ** 0.5)
            return total_car >= cars

        while left <= right:
            mid = (left + right)//2
            if repair(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


        