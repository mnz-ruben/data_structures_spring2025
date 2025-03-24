class MaxHeap:
    def __init__(self):
        # Initialize an empty list to represent the heap.
        self.heap = []

    def isEmpty(self):
        """Return True if the heap is empty."""
        return len(self.heap) == 0

    def parent(self, index):
        """Return the index of the parent of the given node."""
        return (index - 1) // 2

    def leftChild(self, index):
        """Return the index of the left child."""
        return 2 * index + 1

    def rightChild(self, index):
        """Return the index of the right child."""
        return 2 * index + 2

    def insert(self, item):
        """Add an item to the heap and reheapify upward."""
        self.heap.append(item)
        self.reheapifyUp(len(self.heap) - 1)

    def reheapifyUp(self, index):
        """
        Reheapify by sifting the element at 'index' upward
        until the heap property is restored.
        """
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            # Swap with parent if current item is larger.
            self.heap[self.parent(index)], self.heap[index] = (
                self.heap[index],
                self.heap[self.parent(index)]
            )
            index = self.parent(index)

    def remove(self):
        """
        Remove and return the root element (maximum).
        After removal, reheapify downward.
        """
        if self.isEmpty():
            return None  # Or raise an exception.

        root = self.heap[0]
        # Replace the root with the last element.
        last_item = self.heap.pop()
        if not self.isEmpty():
            self.heap[0] = last_item
            self.reheapifyDown(0)
        return root

    def reheapifyDown(self, index):
        """
        Reheapify by sifting the element at 'index' downward
        until the heap property is restored.
        """
        size = len(self.heap)
        while True:
            left = self.leftChild(index)
            right = self.rightChild(index)
            largest = index

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            # Swap current element with the larger child.
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

    def getFront(self):
        """Return the root element (maximum) without removing it."""
        if self.isEmpty():
            return None
        return self.heap[0]

    def __str__(self):
        """Return string representation of the heap."""
        return str(self.heap)


# Testing the MaxHeap implementation
if __name__ == "__main__":
    # Create a max heap instance.
    max_heap = MaxHeap()

    # Test heap addition (insertion) using reheapification (sift-up).
    elements_to_add = [15, 10, 20, 17, 8, 25]
    print("Inserting elements into the heap:")
    for elem in elements_to_add:
        max_heap.insert(elem)
        print(f"After inserting {elem}: {max_heap}")

    print("\nHeap after all insertions:")
    print(max_heap)

    # Test heap removal (deletion) using reheapification (sift-down).
    print("\nRemoving elements from the heap:")
    while not max_heap.isEmpty():
        removed = max_heap.remove()
        print(f"Removed {removed}, Heap now: {max_heap}")

    print("\nFinal heap:", max_heap)
