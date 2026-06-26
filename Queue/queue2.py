class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, element):
        return self.queue.append(element)
        
    def dequeue(self):
        if self.isEmpty():
            return "stack is empty"
        return self.queue.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.queue[0]
        
    def isEmpty(self):
        return len(self.queue) == 0
        
    def size(self):
        return len(self.queue)
        
myqueue = Queue()

while True:
    current_size = myqueue.size()
    
    if current_size < 7:
        user_input = input(f"Enter the number {current_size+1} : ")
    else:
        user_input = input(f"Enter more elements or type done : ")
        
    if user_input.lower() == "done":
        if current_size >= 7:
            break
        else:
            continue
        
    myqueue.enqueue(user_input)
        
print(f"Queue : {myqueue.queue}")
print("show elements : ", myqueue.peek())
print("Dequeued elements : ", myqueue.dequeue())
print("Check if the queue is empty : ", myqueue.isEmpty())
print("Size of the queue : ", myqueue.size())