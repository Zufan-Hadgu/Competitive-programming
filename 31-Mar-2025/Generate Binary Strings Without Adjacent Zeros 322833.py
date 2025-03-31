# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        nums = ["0", "1"]
        if n == 1:
            return ["0", "1"]
        
        def perm(path):
            nonlocal ans
            if len(path) == n:  
                 
                if "1" in path:
                    ans.append("".join(path))
                return

            for num in nums:
                 
                if num == "0" and (len(path) > 0 and path[-1] == "0"):
                    continue   
                
                path.append(num)
                perm(path)
                path.pop()   
        
        perm([])   
        return ans
