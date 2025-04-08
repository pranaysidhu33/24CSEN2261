class Node:
    def __init__(self, data):
        self.data = data  # Data to store
        self.next = None  # Pointer to the next node


class Queue:
    def __init__(self):
        self.front = None  # Front of the queue
        self.rear = None   # Rear of the queue
        self.size = 0      # Size of the queue

    # Method to check if the queue is empty
    def is_empty(self):
        return self.front is None

    # Method to enqueue (add an element) to the queue
    def enqueue(self, data):
        new_node = Node(data)  # Create a new node
        if self.rear is None:
            # If the queue is empty, both front and rear will point to the new node
            self.front = self.rear = new_node
        else:
            # If the queue is not empty, add the new node at the end (rear)
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        print(f"Enqueued {data}")

    # Method to dequeue (remove an element) from the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        # Remove the front element
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:  # If the queue becomes empty after dequeue
            self.rear = None
        self.size -= 1
        print(f"Dequeued {dequeued_data}")
        return dequeued_data

    # Method to get the front element of the queue
    def front_element(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.front.data

    # Method to get the current size of the queue
    def get_size(self):
        return self.size

    # Method to display the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        current = self.front
        print("Queue elements:", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage:
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

queue.display()

print("Front element:", queue.front_element())
print("Size of queue:", queue.get_size())

queue.dequeue()
queue.dequeue()

queue.display()

print("Front element:", queue.front_element())
print("Size of queue:", queue.get_size())
