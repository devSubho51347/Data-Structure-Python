class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    # -------------------------
    # Insert at Beginning
    # -------------------------
    def insert_at_beginning(self, data):
        new_node = Node(data)

        # Empty list
        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            return

        tail = self.head.prev

        new_node.next = self.head
        new_node.prev = tail

        tail.next = new_node
        self.head.prev = new_node

        self.head = new_node

    # -------------------------
    # Insert at End
    # -------------------------
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            return

        tail = self.head.prev

        tail.next = new_node
        new_node.prev = tail

        new_node.next = self.head
        self.head.prev = new_node
        
    def findMiddle(self):
        #code here
        if self.head.next is None:
            return head
        
        temp = self.head
        
        head1 = self.head.next
        head2 = self.head.next.next
        
        
        while (head2 != temp) and (head2.next != temp):
            head1 = head1.next
            head2 = head2.next.next
        return head1.data      

    # -------------------------
    # Print Forward
    # -------------------------
    def print_forward(self):
        if self.head is None:
            print("List is empty")
            return

        curr = self.head

        while True:
            print(curr.data, end=" <-> ")
            curr = curr.next

            if curr == self.head:
                break

        print("(HEAD)")

    # -------------------------
    # Print Backward
    # -------------------------
    def print_backward(self):
        if self.head is None:
            print("List is empty")
            return

        tail = self.head.prev
        curr = tail

        while True:
            print(curr.data, end=" <-> ")
            curr = curr.prev

            if curr == tail:
                break

        print("(TAIL)")
        
        
          
        
cdll = CircularDoublyLinkedList()

cdll.insert_at_end(10)
cdll.insert_at_end(20)
cdll.insert_at_end(30)
cdll.insert_at_end(40)

cdll.insert_at_end(50)
cdll.insert_at_end(60)

cdll.print_forward()       

print(cdll.findMiddle())