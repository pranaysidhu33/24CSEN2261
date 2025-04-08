class Queue:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum size of the queue
        self.queue = [None] * self.capacity  # Array to store queue elements
        self.front = 0  # Index of the front of the queue
        self.rear = -1  # Index of the rear of the queue
        self.size = 0  # Number of elements in the queue

    # Method to check if the queue is full
    def is_full(self):
        return self.size == self.capacity

    # Method to check if the queue is empty
    def is_empty(self):
        return self.size == 0

    # Method to enqueue (add an element) to the queue
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
            return
        self.rear = (self.rear + 1) % self.capacity  # Circular increment
        self.queue[self.rear] = item
        self.size += 1
        print(f"Enqueued {item}")

    # Method to dequeue (remove an element) from the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity  # Circular increment
        self.size -= 1
        print(f"Dequeued {item}")
        return item

    # Method to get the front element of the queue
    def front_element(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[self.front]

    # Method to get the current size of the queue
    def get_size(self):
        return self.size

    # Method to display the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        print("Queue elements:", end=" ")
        for i in range(self.size):
            print(self.queue[(self.front + i) % self.capacity], end=" ")
        print()

# Example usage:
queue = Queue(5)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

queue.display()

print("Front element:", queue.front_element())
print("Size of queue:", queue.get_size())

queue.dequeue()
queue.dequeue()

queue.display()

print("Front element:", queue.front_element())
print("Size of queue:", queue.get_size())
