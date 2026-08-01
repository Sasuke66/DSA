def BFS(root):
    queue = []
    queue.append(root)
    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.pop(0)
            print(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)