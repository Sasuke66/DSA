#traversing a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def traverseData(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end = " -> ")
        currentNode = currentNode.next
    print("null")
        
node1 = Node(4)
node2 = Node(6)
node3 = Node(2)
node4 = Node(9)
node5 = Node(15)
node6 = Node(26)
node7 = Node(0)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

traverseData(node1)