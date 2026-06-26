class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def preorder_traversal(node):
    if node is None:
        return
    print(node.data, end=' ')
    preorder_traversal(node.left)
    preorder_traversal(node.right)

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

preorder_traversal(root)