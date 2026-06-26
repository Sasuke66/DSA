class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_result = self.maxDepth(root.left)
        right_result = self.maxDepth(root.right)
        
        return max(left_result, right_result) + 1