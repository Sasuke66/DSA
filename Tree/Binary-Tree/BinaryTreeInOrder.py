class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.data, end=' ')
    inorder_traversal(node.right)

root = TreeNode('Grandparents')
nodeA = TreeNode('Father')
nodeAA = TreeNode('Mother')
nodeA1 = TreeNode('Anu')
nodeA2 = TreeNode('Adi')

root.left = nodeA
root.right = nodeAA
nodeA.left = nodeA1
nodeA.right = nodeA2
nodeAA.left = nodeA1
nodeAA.right = nodeA2

inorder_traversal(root)