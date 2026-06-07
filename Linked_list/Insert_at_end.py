# Insert at start is o(1) and inser at end O(n):

class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
    
    ### Insert at begin
    def insert_at_end(head,x):
        new_tail = Node(x)
        
        if head is None:
            return Node(key)
        
        while head is not None:
            if head.next is None:
                head.next = new_tail
                print(head.next.key)
                break
                
            head = head.next
        print()    
        print("end")    
    
    def printList(head):
        while head is not None:
            print(head.key)
            head = head.next
            
head = Node(10)
head.next = Node(20)
head.next.next  = Node(30)

head = Node.insert_at_end(head,100)
Node.printList(head)            
    
    
            