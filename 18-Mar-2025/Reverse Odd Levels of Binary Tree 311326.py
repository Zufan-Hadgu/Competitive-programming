# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        # print(queue)
        position = 0
        while queue:
            level_element = []
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if position %2 == 1:
                    level_element.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            l = 0
            r = len(level_element) - 1
           
            while l < r:
                level_element[l].val,level_element[r].val = level_element[r].val,level_element[l].val
                l += 1
                r -= 1

            position += 1

        return root


        