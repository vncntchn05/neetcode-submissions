# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        layers = []

        def dfs(root, depth):
            if not root:
                return None

            while len(layers) < depth + 1:
                layers.append([])
            layers[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)
        ans = []
        print(layers)
        for layer in layers:
            ans.append(layer[-1])

        return ans
