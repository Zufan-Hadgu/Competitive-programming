# Problem: Fizz Buzz - https://leetcode.com/problems/fizz-buzz/description/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr_new = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 ==0:
                arr_new.append("FizzBuzz") 
            elif i % 3 == 0:
                arr_new.append("Fizz")
            elif i % 5 == 0:
                arr_new.append("Buzz")
            else:
                arr_new.append(str(i))
        return arr_new


        