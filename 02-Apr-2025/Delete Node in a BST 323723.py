# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find(cur):
            current = cur
            while current.right:
                current = current.right
            return current
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: 
            if not root.left:
                return root.right
            elif not root.right:
                return root.left 
    
            newval = find(root.left)
            root.val = newval.val
            root.left = self.deleteNode(root.left, newval.val)
        return root
        
        
