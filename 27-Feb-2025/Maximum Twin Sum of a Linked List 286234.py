# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head  
        prev = None
         
        while fast and fast.next:
            fast = fast.next.next
            pointer = slow.next   
            slow.next = prev
            prev = slow
            slow = pointer
        summa = 0
        max_sum = 0
        while prev:
            summa = slow.val + prev.val
            max_sum = max(summa,max_sum)
            slow = slow.next
            prev = prev.next
        return max_sum


       
        

        