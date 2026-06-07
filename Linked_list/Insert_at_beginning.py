class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
    
    ### Insert at begin
    def insert_at_head(head,x):
        new_head = Node(x)
        new_head.next = head
        return new_head
    
    def printList(head):
        while head is not None:
            print(head.key)
            head = head.next
            
head = Node(10)
head.next = Node(20)
head.next.next  = Node(30)

head = Node.insert_at_head(head,100)

Node.printList(head)            
    
    
            