class Node:
    def __init__(self,key):
        self.key = int(key)
        self.next = None
        
    #### Create a search function for the linked list f ot find the position ofa an element
    def search(head,x):
        pos = 1
        while head is not None:
            if head.key == int(x):
                return pos
            pos = pos + 1
            head = head.next
        return -1

head = Node(10)
head.next = Node(20)
head.next.next  = Node(30)

val = Node.search(head,40)
print(val)
        
                