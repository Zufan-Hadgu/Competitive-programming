# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        output = []
        while queue:
            level_size = len(queue)
            average = 0
            for _ in range(level_size):
                node = queue.popleft()
                average += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(average/level_size)
        return output
            
        