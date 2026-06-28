class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def inorder_traversal(root):
    stack = [root]
    
    while (root is not None) or (len(stack) > 0):
        
        while root is not None:
            root = root.left
            stack.append(root)
        
        root = stack.pop()
        print(root.data)
        
        ## Now move to the right direction
        root = root.right            
        