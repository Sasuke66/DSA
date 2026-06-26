class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data, end=' ')

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

postorder_traversal(root)