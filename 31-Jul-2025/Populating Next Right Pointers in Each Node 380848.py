# Problem: Populating Next Right Pointers in Each Node - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            prev_node = None
            
            for _ in range(level_size):
                node = queue.popleft()
                
                if prev_node:
                    prev_node.next = node
                prev_node = node
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root