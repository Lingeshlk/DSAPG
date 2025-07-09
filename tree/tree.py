class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Build tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Traversals
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=' ')

def preorder(node):
    if node:
        print(node.value, end=' ')
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=' ')

# Run
print("Inorder Traversal:")
inorder(root)        # Output: 4 2 5 1 3

print("\nPreorder Traversal:")
preorder(root)       # Output: 1 2 4 5 3

print("\nPostorder Traversal:")
postorder(root)      # Output: 4 5 2 3 1
