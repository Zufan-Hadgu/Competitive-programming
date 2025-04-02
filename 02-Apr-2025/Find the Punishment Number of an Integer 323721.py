# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        answer = 0
        added_numbers = set()
        
        def split(i, path, remaining):
            nonlocal answer
             
            if not remaining:
                if sum(path) == i and i ** 2 not in added_numbers:
                    answer += i ** 2
                    added_numbers.add(i ** 2)
                 
            for j in range(1, len(remaining) + 1):
                path.append(int(remaining[:j]))  
                split(i, path, remaining[j:])    
                path.pop()   
        
        for i in range(1, n + 1):
            split(i, [], str(i ** 2))   
        return answer
