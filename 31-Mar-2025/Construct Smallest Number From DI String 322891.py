# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # n = len(pattern)
        # stack = []
        # result = []
        
         
        # for i in range(n + 1):   
        #     stack.append(i + 1)
            
             
        #     if i == n or pattern[i] == 'I':
                 
        #         while stack:
        #             result.append(str(stack.pop()))
        
        # return "".join(result)
   
        n = len(pattern)
        result = []
        nums = [str(i) for i in range(1, n + 2)]

        def backtrack(path):
            if len(path) == n + 1:
                result.append("".join(path))
                return

            for num in nums:
                if num in path:
                    continue
                if len(path) == 0 or (pattern[len(path)-1] == 'I' and int(path[-1]) < int(num)) or (pattern[len(path)-1] == 'D' and int(path[-1]) > int(num)):
                    path.append(num)
                    backtrack(path)
                    path.pop()

        backtrack([])

        return min(result)

