### define class to create nodes of the tree
class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


### Use the diameter as a global variable        
dia = 0        
        
def getDiameter(root):
    
    if root is None:
        return 0
    
    lh = getDiameter(root.left)
    rh = getDiameter(root.right)
    
    global dia
    
    dia = max(dia,lh+rh)
    
    return 1 + max(lh,rh)

A = Tree(5)
B = Tree(5)
C= Tree(5)
D= Tree(5)
E= Tree(5)
        
A.left = B
A.right = C
C.left = D
D.right = E

getDiameter(A)

print(dia)        