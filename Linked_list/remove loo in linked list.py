class Node:
    def __init__(self,val):
        self.next=None
        self.data=val
    
    
def removeLoop(head):
    # code here
    
    if head is None:
        return head
        
    li = []
    temp = head
    head1 = head
    head2 = head.next.next
    
    # while (head2 is not None) and (head2.next is not None):
    while head1.next is not None:
        
        
        if head1.next in li:
            head1.next = None
            return temp
        
        else:    
            li.append(head1)
        head1 = head1.next
        # head2 = head2.next.next
    return temp

def detectLoop(head):
    if head is None:
        return False
        
    li = []
    temp = head
    head1 = head
    head2 = head.next.next
    
    while (head2 is not None) and (head2.next is not None):
    # while head1.next is not None:
        
        
        if head1 == head2:
            # head1.next = None
            return True
        
        # else:    
            li.append(head)
        head1 = head1.next
        head2 = head2.next.next
    return False
    


A = Node(1)
B = Node(2)
C = Node(3)

A.next = B
B.next = C
C.next = B

print("Is loop present in the linked list", detectLoop(A))

# print(removeLoop(A))


print("Is loop present in the linked list", detectLoop(removeLoop(A)))

### Solved part 1 detection of loop is done 