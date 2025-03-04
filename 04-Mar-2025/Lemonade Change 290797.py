# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False

        countF = 0
        countT = 0

        for bill in bills:
            if bill == 5:
                countF += 1
            elif bill == 10:
                if countF >= 1:
                    countT += 1
                    countF -= 1
                else:
                    return False
            elif bill == 20:
                if (countF >= 1 and countT >= 1):
                    countF -= 1
                    countT -= 1
                 
                elif countF >= 3:
                    countF -= 3
                else:
                    return False
        return True
                


 