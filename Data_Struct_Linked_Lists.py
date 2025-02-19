#Defining the Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Creating a Linked List

class LinkedList:
    def __init__(self):
        self.head = None #This helps establish that the list is initially empty

    #Inserting New Nodes to the end
    def insert(self, data):
        new_node = Node(data) #This is how create a Node
        if self.head is None: #Basically if the list is empty then set head to new node
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next # go to the last node
        temp.next = new_node #links last node to new node

    #deleting a node by value
    def delete(self, key):
        temp = self.head

        #if head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        #search for the key and track previous
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None: #if key is not found
            return

        prev.next = temp.next #unlink the node first
        temp = None

    #Display the linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end =" -> ")
            temp = temp.next
        print("None") #End of list


#Creating the linked list
ll = LinkedList()
ll.insert(5)
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(0)

#Display the List
ll.display()



