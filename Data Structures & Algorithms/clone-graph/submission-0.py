"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = set()
        nodes = [None] * 101
        
        def dfs(node):
            if not node:
                return None
            visited.add(node)

            dupe = Node(node.val, [])
            nodes[node.val] = dupe

            for nei in node.neighbors:
                if nei not in visited:
                    dupe.neighbors.append(dfs(nei))
                else:
                    dupe.neighbors.append(nodes[nei.val])

            return dupe

        return dfs(node)