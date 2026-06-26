class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        right = self.invertTree(root.left)
        left = self.invertTree(root.right)
        root.right = right
        root.left = left

        return root