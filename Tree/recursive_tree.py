class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

def preorder(root):
    if root is None:
        return
    
    print(root.data)
    inorder(root.left)
    inorder(root.right)
    
def inorder(root):
    
    if root is None:
        return
    
    inorder(root.left)
    print(root.data)
    inorder(root.right)
    
def postorder(root):
    if root is None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.data)        
    
            
# Creating tree
A = Tree(5)
B = Tree(6)
C = Tree(7)

D = Tree(8)
E = Tree(9)
F = Tree(10)

A.left = B
A.right = C

B.left = D
B.right = E
E.right = F    

preorder(A)

print("------------------------------------")   

inorder(A)    

print("------------------------------------")   

postorder(A)    