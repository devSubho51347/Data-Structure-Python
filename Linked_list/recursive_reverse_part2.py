class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        
    #### Create teh recursive function for reverse of the linked list 
    ### the function should return the new head
    ### 10- 20-30-40
    
    def reverse(head, prev = None):
        if head is None:
            return prev
        
        curr = head
        nxt = head.next
        prev = prev
        curr.next = prev
        prev = curr
        
        return Node.reverse(nxt,prev)
    
    ### Print all the elements of a linked list
    def printList(head):
        while head is not None:
            print(head.key)
            head = head.next
            
                
head = Node(10)
head.next = Node(20)
head.next.next  = Node(30)
head.next.next.next  = Node(40)

Node.printList(head)    

reversed_head = Node.reverse(head,None)

Node.printList(reversed_head)   

        