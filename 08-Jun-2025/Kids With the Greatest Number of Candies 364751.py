# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_can  = max(candies)
        output = []
        for candy in candies:
            if candy + extraCandies >= max_can:
                output.append(True)
            else:
                output.append(False)
        return output 



        