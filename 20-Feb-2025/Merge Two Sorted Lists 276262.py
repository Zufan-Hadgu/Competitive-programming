# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode()
        last = new_node
        while list1 and list2:
            if list1.val < list2.val:
                last.next = list1
                list1 = list1.next
            else:
                last.next = list2
                list2 = list2.next
            last = last.next
        if list1:
            last.next = list1
           
        if list2:
            last.next = list2    
        return new_node.next
    

            


        