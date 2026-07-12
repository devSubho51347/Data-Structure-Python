class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

def get_height(root):
    if root is None:
        return 0
    
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    
    if (left_height == -1) or (right_height == -1) or (abs(left_height - right_height) > 1):
        return -1
    
    
    
    
    return 1 + max(left_height,right_height)


def balanced_tree(root):
    if get_height(root) == -1:
        print("The tree is not balanced")
    else:
        print("The tree is balanced")    
        
        
A = Tree(5)
B = Tree(5)
C= Tree(5)
D= Tree(5)
E= Tree(5)
        
A.left = B
A.right = C

# C.left = D

# D.left = E

balanced_tree(A)        