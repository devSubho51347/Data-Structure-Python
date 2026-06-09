class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        
    #### Create teh recursive function for reverse of the linked list 
    ### the function should return the new head
    ### 10- 20-30-40
    
    def reverse(head):
        if head.next is None:
            return head
        
        reverse_head = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return reverse_head
          