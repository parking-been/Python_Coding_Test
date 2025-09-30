
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data,end=" ")

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')

print("inorder: ") 
inorder(root)
print("\npreorder: ")
preorder(root)
print("\npostorder: ")
postorder(root)

"""
inorder: 
D B E A C
preorder:
A B D E C
postorder:
D E B C A
"""