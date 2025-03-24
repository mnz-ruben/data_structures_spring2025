class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        # Initially, the queue is empty; tail is None.
        self.tail = None

    def isEmpty(self):
        """Return True if the queue is empty, else False."""
        return self.tail is None

    def enqueue(self, item):
        """Insert an item at the rear of the queue."""
        new_node = Node(item)
        if self.isEmpty():
            # When queue is empty, new_node points to itself.
            self.tail = new_node
            self.tail.next = new_node
        else:
            # new_node.next points to the front of the queue (tail.next)
            new_node.next = self.tail.next
            # Insert new_node after tail
            self.tail.next = new_node
            # Update tail to be the new node.
            self.tail = new_node

    def dequeue(self):
        """Remove the front item from the queue."""
        if self.isEmpty():
            print("Queue is empty. Cannot dequeue.")
            return

        front = self.tail.next  # The front of the queue.
        if self.tail == front:
            # Only one element was present.
            self.tail = None
        else:
            # Remove the front node by linking tail directly to front.next.
            self.tail.next = front.next

    def getFront(self):
        """Return the front element of the queue without removing it."""
        if self.isEmpty():
            print("Queue is empty. No front element.")
            return None
        return self.tail.next.data

# Example usage:
if __name__ == "__main__":
    cq = CircularQueue()
    print("Is queue empty?", cq.isEmpty())  # Expected: True

    # Enqueue elements
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    print("Front element:", cq.getFront())  # Expected: 10

    # Dequeue one element and check front
    cq.dequeue()
    print("Front element after one dequeue:", cq.getFront())  # Expected: 20

    # Dequeue all elements
    cq.dequeue()
    cq.dequeue()
    print("Is queue empty after removing all elements?", cq.isEmpty())  # Expected: True
