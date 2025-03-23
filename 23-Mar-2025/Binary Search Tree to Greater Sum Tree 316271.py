# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
         
        node_val = 0   

        def bst(node):
            nonlocal node_val
            if not node:
                return

            
            bst(node.right)
            node_val += node.val
            node.val = node_val
            bst(node.left)

        bst(root)
        return root


        
         
        # node_val = 0
        # def bst(root):
        #     if not root:
        #         return 0
        #     if root.val > root.left.val or root.val > root.right.val:
        #         node_val += root.val
        #     right = bst(root.right)
        #     left = bst(root.left)
        #     ans.append(node_val)

        # return ans


        