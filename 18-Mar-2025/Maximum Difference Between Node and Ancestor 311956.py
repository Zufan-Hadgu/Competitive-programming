# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = []
        def differ(root):
            if not root:
                return [float('inf'),float('-inf')]
            left = differ(root.left)
            right = differ(root.right)

            ans.append(abs(root.val-left[0]))
            ans.append(abs(root.val-right[0]))
            ans.append(abs(root.val-left[1]))
            ans.append(abs(root.val-right[1]))
            return [min(left[0] , right[0] , root.val) , max(right[1] , left[1] , root.val)]

        differ(root)
        temp = 0

        for i in ans:
            if i != float("inf"):
                temp = max(temp , i)
        return temp
         


        