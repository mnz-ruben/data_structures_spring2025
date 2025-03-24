class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

def DoubleLinkedlistInsert(data, index, Ptr):
    new_node = Node(data)
    if index < 0:
        return -1  # Invalid index

    if Ptr.head is None:
        if index == 0:
            Ptr.head = new_node
            return 0
        else:
            return -1  # Cannot insert at non-zero index in empty list

    if index == 0:
        new_node.next = Ptr.head
        Ptr.head.prev = new_node
        Ptr.head = new_node
        return 0

    current = Ptr.head
    i = 0
    while current is not None and i < index - 1:
        current = current.next
        i += 1

    if current is None:
        return -1  # Index out of bounds

    new_node.next = current.next
    new_node.prev = current
    if current.next is not None:
        current.next.prev = new_node
    current.next = new_node
    return 0

def DoubleLinkedlistDelete(index, Ptr):
    if Ptr.head is None or index < 0:
        return -1  # Nothing to delete

    current = Ptr.head
    if index == 0:
        Ptr.head = current.next
        if Ptr.head is not None:
            Ptr.head.prev = None
        return 0

    i = 0
    while current is not None and i < index:
        current = current.next
        i += 1

    if current is None:
        return -1  # Index out of bounds

    if current.prev is not None:
        current.prev.next = current.next
    if current.next is not None:
        current.next.prev = current.prev
    return 0

dll = DoubleLinkedList()
DoubleLinkedlistInsert(10, 0, dll)
DoubleLinkedlistInsert(20, 1, dll)
DoubleLinkedlistInsert(15, 1, dll)
DoubleLinkedlistDelete(1, dll)

# Print list to verify
curr = dll.head
while curr:
    print(curr.data, end=' ')
    curr = curr.next
# Output: 10 20
