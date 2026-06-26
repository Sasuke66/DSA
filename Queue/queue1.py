queue = []

#enqueue
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue : ", queue)

#peek
showElement = queue[0]
print("Peek : ", showElement)

#size
size = len(queue)
print("Size of the queue : ", size)

#dequeue
poppedElement = queue.pop(0)
print("Dequeued element : ", poppedElement)

#peek
showElement = queue[0]
print("Peek : ", showElement)

#isEmpty
isEmpty = not bool(queue)
print("IsEmpty : ", isEmpty)

#size
size = len(queue)
print("Size of the queue : ", size)