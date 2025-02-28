# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
                

        def reverse(head,k):
            prev = None
            current = head
            length = 0
            while current and length < k:
                new_node = current.next
                current.next = prev
                prev  = current
                current = new_node
                length += 1
            return prev


        current = head
        length = 0
        while current:
            length += 1
            current = current.next
            
       
    
        dummy = ListNode()
        mod = dummy
        fast = head
        slow = head
        while slow and length >= k:

            for _ in range(k):
                fast = fast.next

            new_node = reverse(slow,k)
            mod.next = new_node
            mod = slow
            slow = fast
            length -= k
        mod.next = slow
        return dummy.next

            
            
             
        

            
            



        

            