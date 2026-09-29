# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
            
        n = len(nodes) 
        for i in range(n // 2):
            nodes[i].next = nodes[n - 1 - i]
            nodes[n - 1 - i].next = nodes[i + 1]
        nodes[n // 2].next = None
