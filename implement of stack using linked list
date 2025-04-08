class Node:
    def __init__(self, data):
        self.data = data  # Data to store
        self.next = None  # Pointer to the next node


class Stack:
    def __init__(self):
        self.top = None  # The top of the stack
        self.size = 0     # Size of the stack

    # Method to check if the stack is empty
    def is_empty(self):
        return self.top is None

    # Method to push an element onto the stack
    def push(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.top  # Point new node to the current top
        self.top = new_node  # Update the top to the new node
        self.size += 1
        print(f"Pushed {data}")

    # Method to pop an element from the stack
    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        popped_data = self.top.data
        self.top = self.top.next  # Move the top pointer to the next node
        self.size -= 1
        print(f"Popped {popped_data}")
        return popped_data

    # Method to get the top element of the stack
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.top.data

    # Method to get the current size of the stack
    def get_size(self):
        return self.size

    # Method to display the stack
    def display(self):
        if self.is_empty():
            print("Stack is empty!")
            return
        current = self.top
        print("Stack elements:", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
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
