# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        less_l = ListNode()
        more_l = ListNode()
        # print("less_l" less_l)
        less = less_l
        more = more_l
        
        # print(less)

        current = head
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                more.next = current
                more = more.next

            current = current.next
        less.next = more_l.next
        more.next = None

        return less_l.next
        # print(less)
        # print(more)
        

        