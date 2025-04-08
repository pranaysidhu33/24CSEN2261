class Stack:
    def __init__(self):
        self.stack = []  # List to store stack elements

    # Method to check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Method to push an element onto the stack
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item}")

    # Method to pop an element from the stack
    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        item = self.stack.pop()  # Remove and return the top element
        print(f"Popped {item}")
        return item

    # Method to get the top element of the stack
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack[-1]

    # Method to get the current size of the stack
    def get_size(self):
        return len(self.stack)

    # Method to display the stack
    def display(self):
        if self.is_empty():
            print("Stack is empty!")
            return
        print("Stack elements:", end=" ")
        for item in reversed(self.stack):
            print(item, end=" ")
        print()

# Example usage:
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

stack.display()

print("Top element:", stack.peek())
print("Size of stack:", stack.get_size())

stack.pop()
stack.pop()

stack.display()

print("Top element:", stack.peek())
print("Size of stack:", stack.get_size())
