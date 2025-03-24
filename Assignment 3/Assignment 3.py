class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None


def push(T, stack):
    """Insert element T onto the top of the stack.
       Returns 0 on success."""
    new_node = StackNode(T)
    new_node.next = stack.top
    stack.top = new_node
    return 0  # success


def topandpop(stack):
    """Return the top element of the stack and remove it.
       Returns the element's value, or -1 if the stack is empty."""
    if stack.top is None:
        return -1  # error: stack is empty
    top_value = stack.top.data
    stack.top = stack.top.next  # remove the top element
    return top_value


# Example usage:
if __name__ == "__main__":
    s = Stack()
    push(10, s)
    push(20, s)
    push(30, s)

    print("Top and pop:", topandpop(s))  # Should print 30
    print("Top and pop:", topandpop(s))  # Should print 20
    print("Top and pop:", topandpop(s))  # Should print 10
    print("Top and pop:", topandpop(s))  # Should print -1, as the stack is empty
