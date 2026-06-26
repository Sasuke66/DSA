class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, element):
        self.stack.append(element)
        
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
        
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
        
    def isEmpty(self):
        return len(self.stack) == 0
        
    def size(self):
        return len(self.stack)
        
mystack = Stack()

while True:
    current_size = mystack.size()
    
    if current_size < 7:
        user_input = input(f"Enter the element {current_size + 1}: ")
    else:
        user_input = input("Enter an element (or type 'done' to finish): ")
        
    if user_input.lower() == "done":
        if current_size >= 7:
            break
        else:
            print(f"We only have {current_size} elements we need more!!")
            continue
        
    mystack.push(user_input)    

print(f"Stack : {mystack.stack}")
print("peek : ", mystack.peek())
print("pop : ", mystack.pop())
print("peek : ", mystack.peek())
        