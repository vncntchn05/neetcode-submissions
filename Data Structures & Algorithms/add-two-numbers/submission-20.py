# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        curr = head

        while True:
            if l1 and l2:
                curr.next = ListNode((l1.val + l2.val + carry) % 10)
                curr = curr.next
                carry = (l1.val + l2.val + carry) // 10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                curr.next = ListNode((l1.val + carry) % 10)
                curr = curr.next
                carry = (l1.val + carry) // 10
                l1 = l1.next
            elif l2:
                curr.next = ListNode((l2.val + carry) % 10)
                curr = curr.next
                carry = (l2.val + carry) // 10
                l2 = l2.next
            else:
                if carry:
                    curr.next = ListNode(carry)
                break

        return head.next