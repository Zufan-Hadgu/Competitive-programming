# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(node,pathsum,result):
            pathsum += node.val
            if not node.left and not node.right:
                return result.append(pathsum)
            if node.left:
                dfs(node.left,pathsum,result)
            if node.right:
                dfs(node.right,pathsum,result)
        result = []
        dfs(root,0,result)
        if targetSum in result:
            return True
        else:
            return False
        
        