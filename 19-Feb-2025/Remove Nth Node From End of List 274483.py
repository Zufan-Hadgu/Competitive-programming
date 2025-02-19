# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
            
        idx = 0 
        current=head
  
        if length == n:
            head = head.next
            return head


        while current:
            if idx == length -n -1:
                current.next = current.next.next
                return head
            idx += 1
            current = current.next

        




         
        