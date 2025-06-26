# Problem: Range Sum of BST - https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if not root:
            return 0
        queue = deque([root])
        output = 0
        while queue:
            node = queue.popleft()
            if node.val >= low and node.val <= high:
                output += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return output

