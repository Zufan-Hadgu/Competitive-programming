# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = ListNode()
        odd = ListNode()
        odd_node = odd
        even_node = even
        current = head
        count = 1

        while current:
            if count % 2 != 0:   
                New_odd_node = ListNode(current.val)
                odd_node.next = New_odd_node
                odd_node = odd_node.next   
                
            else:   
                New_even_node = ListNode(current.val)
                even_node.next = New_even_node
                even_node = even_node.next   
               
            count += 1
            current = current.next

        odd_node.next = even.next   
        even_node.next = None   
        return odd.next   
