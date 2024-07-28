class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")


parent = Node(1)
parent.left = Node(2)
parent.right = Node(3)
parent.left.left = Node(4)
parent.left.right = Node(5)
parent.right.left = Node(6)
parent.right.right = Node(7)

print("Inorder traversal of binary tree is:")
inorder(parent)
print("\nPreorder traversal of binary tree is: ")
preorder(parent)
print("\nPostorder traversal of binary tree is")
postorder(parent)
