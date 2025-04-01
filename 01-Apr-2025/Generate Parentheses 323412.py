# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        paren = ['(',')']
        ans = []
        if n == 1:
            return ["()"]
        
        def perm(path,open,close):
            nonlocal ans
            if len(path) == 2*n:
                ans.append("".join(path))
                return
            if open < n:
                path.append('(')
                print(path)
                perm(path,open + 1,close)
                path.pop()
            if close < open:
                path.append(')')
                print(path)
                perm(path,open ,close+1)
                path.pop()
           
            
                # if (len(path) == 1 and path[-1] == ')'):
                #     continue
                # path.append(sign)
                # path.pop()
        perm([],0,0)
        return ans

        