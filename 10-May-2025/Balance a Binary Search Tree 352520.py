# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums=[]
        def inorder(current):
            if current:
                inorder(current.left)
                nums.append(current.val)
                inorder(current.right)
        inorder(root)
        return self.sortedArrayToBST(nums)    
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid=len(nums)//2
        if not nums:
            return None
        root=TreeNode(nums[mid])
        root.left=self.sortedArrayToBST(nums[:mid])
        root.right=self.sortedArrayToBST(nums[mid+1:])
        return root
        