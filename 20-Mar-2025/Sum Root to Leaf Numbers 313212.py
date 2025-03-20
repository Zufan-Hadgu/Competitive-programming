# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        number = 0
        def adding(root,number):
            if root is None:
                return 0
            number = number * 10 + root.val
            if root.left is None and root.right is None:
                return number
            return adding(root.left,number) + adding(root.right,number)
        return adding(root,0)
          
        
