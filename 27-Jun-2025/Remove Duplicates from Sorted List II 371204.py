# Problem: Remove Duplicates from Sorted List II - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        counts = Counter(values)
        unique_values = [val for val in values if counts[val] == 1]

        dummy = ListNode(0)
        current = dummy
        for val in unique_values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next

      


        
        