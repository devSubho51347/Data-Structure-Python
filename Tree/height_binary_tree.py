class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

def find_height(root):
    if root is None:
        return 0 
    
    left_height = find_height(root.left)
    right_height = find_height(root.right)
    
    return 1 + max(left_height, right_height)

A = Tree(5)
B = Tree(5)
C= Tree(5)
D= Tree(5)
E= Tree(5)
        
A.left = B
A.right = C

C.left = D

D.left = E

print(find_height(A))