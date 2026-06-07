### space -= O(1); Time Complexity O(n)

class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
    
    ### Print all the elements of a linked list
    def printList(head):
        while head is not None:
            print(head.key)
            head = head.next
            

head = Node(10)
head.next = Node(20)
head.next.next  = Node(30)

Node.printList(head)               
        
    