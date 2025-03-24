# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        
        def average(root,add,length):
            nonlocal count
           
            if not root:
                return 0, 0
           
        
            add += root.val
            length += 1 


            left_add , left_l = average(root.left,add,length)
            right_add,right_l = average(root.right,add,length)

            total = left_add + right_add + root.val
            total_length =  left_l + right_l + 1

            # print(total_length)

            if (total//total_length ) == root.val:
                count += 1
            print(count)
            return total , total_length
        average(root,0,0)
        return count
    
        

        