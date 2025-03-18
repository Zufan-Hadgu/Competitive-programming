# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        position = 0
        while queue:
            level_element = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level_element.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if position % 2 == 1:
                result.append(level_element[::-1])
            else:
                result.append(level_element)
            position += 1
        return result

        