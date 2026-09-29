# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        curr = head
        for i in range(length):
            print(curr.val, i, length - n)
            if i + 1 == length - n:
                curr.next = curr.next.next if curr.next != None else None
                break
            elif length == 1:
                return None
            elif i == length - n:
                return head.next
            curr = curr.next

        return head