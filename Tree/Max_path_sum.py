class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


### Use the diameter as a global variable        
path_sum = 0 

def getMaxSum(root):
    if root is None:
        return 0
    left_sum = getMaxSum(root.left)
    right_sum = getMaxSum(root.right)
    
    global path_sum
    
    path_sum = max(path_sum,root.data + (left_sum + right_sum) )
    
    return root.data + max(left_sum,right_sum)


A = Tree(5)
B = Tree(5)
C= Tree(5)
D= Tree(5)
E= Tree(200)
F = Tree(400)
        
A.left = B
A.right = C
C.left = D
C.right = E
E.right = F

getMaxSum(A)

print(path_sum)   