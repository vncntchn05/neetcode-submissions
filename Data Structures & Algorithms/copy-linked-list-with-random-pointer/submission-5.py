"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        nodes = {}
        nodes_list = []
        ans_nodes = []
        curr = head
        length = 0
        while curr:
            new_node = Node(curr.val)
            nodes_list.append(curr)
            ans_nodes.append(new_node)
            nodes[curr] = length
            length += 1
            curr = curr.next

        for i, node in enumerate(nodes_list):
            if i == length - 1:
                ans_nodes[i].next = None
            else:
                ans_nodes[i].next = ans_nodes[i + 1]

            if node.random == None:
                ans_nodes[i].random = None
            else:
                ans_nodes[i].random = ans_nodes[nodes[node.random]]

        return ans_nodes[0]
            


        

        

        