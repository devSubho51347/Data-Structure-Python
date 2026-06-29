#### DFS implementation using stack

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#### Preorder traversal

def print_tree(root):
    if root is None:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.data)

        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)


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

print_tree(A)

##Level Order Traversal using Queue

from collections import deque

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_tree(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()

        print(node.data)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


# Creating tree
A = Tree(5)
B = Tree(6)
C = Tree(7)

A.left = B
A.right = C

print_tree(A)