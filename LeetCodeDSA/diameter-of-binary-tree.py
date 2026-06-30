class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0,0
            leftdiameter,leftlength = dfs(node.left)
            rightdiameter,rightlength = dfs(node.right)
            currHeight = 1 + max(leftlength,rightlength)
            currDia = max(leftdiameter, rightdiameter, (leftlength+rightlength))
            return currDia,currHeight
        return dfs(root)[0]