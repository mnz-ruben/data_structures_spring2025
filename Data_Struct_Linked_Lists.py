class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty list

    # Inserting at a specific index
    def LinkedListInsert(self, data, index):
        new_node = Node(data)

        # Insert at the beginning
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return 1  # Success

        temp = self.head
        for i in range(index - 1):
            if temp is None:  # If index is out of range
                return -1  # Failure
            temp = temp.next

        if temp is None:
            return -1  # Failure

        new_node.next = temp.next
        temp.next = new_node
        return 1  # Success

    # Deleting at a specific index
    def LinkedListDelete(self, index):
        if self.head is None:  # Empty list
            return -1  # Failure

        temp = self.head

        # If deleting the head node
        if index == 0:
            self.head = temp.next
            temp = None
            return 1  # Success

        prev = None
        for i in range(index):
            prev = temp
            temp = temp.next
            if temp is None:
                return -1  # Failure (index out of range)

        prev.next = temp.next
        temp = None
        return 1  # Success

    # Display function to check the list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")  # End of list


# Test the functions
ll = LinkedList()
ll.LinkedListInsert(5, 0)  # Insert at index 0
ll.LinkedListInsert(1, 1)  # Insert at index 1
ll.LinkedListInsert(2, 1)  # Insert at index 1 (shifts 1 forward)
ll.LinkedListInsert(3, 2)  # Insert at index 2

ll.display()  # Expected: 5 -> 2 -> 3 -> 1 -> None

ll.LinkedListDelete(1)  # Delete node at index 1 (removes 2)
ll.display()  # Expected: 5 -> 3 -> 1 -> None
