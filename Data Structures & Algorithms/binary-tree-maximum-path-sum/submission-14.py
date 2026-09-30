# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')

        def dfs(node):
            nonlocal ans
            if not node:
                return 0

            maxl = dfs(node.left)
            maxr = dfs(node.right)

            maxp = max(max(maxl, maxr) + node.val, 0, node.val)
            ans = max(ans, maxl + node.val + maxr, max(maxl, maxr) + node.val, node.val)

            print(node.val, maxp)
            return maxp

        dfs(root)
        return ans