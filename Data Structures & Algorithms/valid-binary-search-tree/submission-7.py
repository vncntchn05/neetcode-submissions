# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        flag = True
        
        def dfs(node):
            nonlocal flag
            if not node:
                return (1000000001, -1000000001)

            sl, gl = dfs(node.left)
            sr, gr = dfs(node.right)

            if node.val <= gl or node.val >= sr:
                flag = False
            return (min(sl, node.val), max(gr, node.val))

        dfs(root)
        return flag