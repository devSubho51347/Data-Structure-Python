"""
Structure of doubly linked list node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        if head is None:
            return None
        
        if head.next is None:
            return head
        previous = None    
        while head is not None:
            curr = head
            nxt = head.next
            
            # if previous is None:
            curr.next = previous
            previous = curr
            previous.prev = nxt
            head = nxt
            
            if head is None:
                return previous
            
            # else:
        return head   