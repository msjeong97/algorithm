# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current_node = result
        carry = 0

        while True:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val_sum = val1 + val2 + carry

            carry = 1            if val_sum >= 10 else 0
            out   = val_sum - 10 if val_sum >= 10 else val_sum
            current_node.val = out

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 or l2 or carry:
                next_node = ListNode()
                current_node.next = next_node
                current_node = next_node
            else:
                break
        
        return result
