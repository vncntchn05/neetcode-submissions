# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        
        def dfs(node, greatest):
            nonlocal ans
            if not node:
                return None

            if node.val >= greatest:
                ans += 1

            dfs(node.left, max(greatest, node.val))
            dfs(node.right, max(greatest, node.val))

        dfs(root, -101)
        return ans