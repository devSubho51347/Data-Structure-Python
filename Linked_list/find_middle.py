class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        
    ## Find the middle element
    
    def find_middle(head):
        curr = head
        jumper = head
        
        if (jumper is None) or (jumper.next is None):
            return curr.key
        
        while (jumper is not None) and (jumper.next is not None):
            curr = head.next
            jumper = head.next.next
            head = head.next
            
        return curr.key   
    
    def printList(head):
        while head is not None:
            print(head.key)
            head = head.next
            

head = Node(10)
head.next = Node(20)
head.next.next  = Node(300)
head.next.next.next  = Node(600)

Node.printList(head)  

print(Node.find_middle(head)) 
            
        
            
        