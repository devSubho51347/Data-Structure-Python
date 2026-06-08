class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
    
    
    def reverse_linked_list(head):
        curr = head
        prev = None
        nxt = None
        
        while curr:
            nxt = curr.next
            # nxt.next = curr
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
            