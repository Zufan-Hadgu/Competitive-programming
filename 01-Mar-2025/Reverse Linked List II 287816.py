# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
      
        leftPrev = dummy
        
        for _ in range(left - 1):
            leftPrev = leftPrev.next
        current = leftPrev.next
             
        
        prev = None
        for i in range(right - left + 1):
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
            
        leftPrev.next.next = current
        leftPrev.next = prev
        return dummy.next




        # def reverse(head):
        #     prev = None
        #     current = head
        #     while current:
        #         next_node = current.next
        #         current.next = prev
        #         prev = current
        #         current = next_node
        #     return prev

        # left_node = head
        # right_node = head
        
        # for _ in range(left):
        #     left = left.next
         
        # for _ in range(right):
        #     right = right.next

        # while left != right.next:
        #     reverse(left)
        #     left = left.next


        
    