class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def length(self):
        return self.size

    def pop(self):
        if self.isEmpty():
            return "Operation cannot be performed"

        popped_value = self.head.key
        self.head = self.head.next
        self.size -= 1

        return popped_value

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.key

    def print_stack(self):
        curr = self.head
        while curr is not None:
            print(curr.key)
            curr = curr.next