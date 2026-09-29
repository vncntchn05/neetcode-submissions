# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        ind = 0

        def dfs(node):
            nonlocal ans
            nonlocal ind
            if not node:
                return

            dfs(node.left)
            ind += 1

            if ind == k:
                ans = node.val

            dfs(node.right)

        dfs(root)
        return ans