# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # length = 0
        # current = head
        # while current:
        #     length += 1
        #     current = current.next
        # current = head
        # right = head
        
        # for _ in range(length):
        #     right = right.next
        # while length > n

        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

        
      

        