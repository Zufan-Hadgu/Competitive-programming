# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        def dfs(node,pathsum,result,output):
            pathsum += node.val
            result.append(node.val)
            if not node.left and not node.right and pathsum == targetSum:
                output.append(list(result))
                   
            if node.left:
                dfs(node.left,pathsum,result,output)
            if node.right:
                dfs(node.right,pathsum,result,output)
            result.pop()
        output = []
        dfs(root,0,[],output)
        return output
            


        