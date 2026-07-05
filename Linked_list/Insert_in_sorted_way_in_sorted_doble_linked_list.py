'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
    #code here
        if x <= head.data:
            new = Node(x)
            new.next = head
            head.prev = new
            return new
            
        ### while head is not None:
        
        temp = head
        
        while head.next is not None:
            
            if (x >= head.data) and (x <= head.next.data):
                new = Node(x)
                new.next = head.next
                head.next.prev = new
                new.prev = head
                head.next = new
                
                return temp
                
            head = head.next       
                
        if head.next is None:
            new = Node(x)
            head.next = new
            new.prev = head
            return temp
        
         
        