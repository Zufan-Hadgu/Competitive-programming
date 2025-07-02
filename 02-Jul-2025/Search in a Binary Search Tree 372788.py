# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def find(root,val):
            if root is None:
                return None
            if val == root.val:
                return root
            if val > root.val:
                return find(root.right,val)
                

            if val < root.val:
                return find(root.left,val)
               
        ans = find(root,val)
        return ans
            


        