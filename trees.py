class Node:
    def __init__ (self,data):
        self.left = None
        self.right = None
        self.data = data
#     def inorder(self):
#         if self.left:
#             self.left.inorder()
#         print(self.data)
#         if self.right:
#             self.right.inorder()

#     def preorder(self):
#         print(self.data)
#         if self.left:
#             self.left.preorder()
#         if self.right:
#             self.right.preorder()

#     def postorder(self):
#         if self.left:
#             self.left.postorder()
#         if self.right:
#             self.right.postorder()
#         print(self.data)


#     def __str__(self):
#         return str(self.data)
    
    
# root = Node(10)
# root.left = Node(20)
# root.right = Node(30)
# root.left.left = Node(40)
# root.left.right = Node(50)
# root.right.left = Node(60)
# root.right.right = Node(70)
# print(root.inorder())
# print(root.preorder())
# print(root.postorder())

#without class
def inorder(node):
    if node!=None:
        inorder(node.left)
        print(node.data,end=" ")
        inorder(node.right)
def preorder(node):
    if node!=None:
        print(node.data,end=" ")
        preorder(node.left)
        preorder(node.right)
def postorder(node):
    if node!=None:
        postorder(node.left)
        postorder(node.right)
        print(node.data,end=" ")
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
print(inorder(root))
print(preorder(root))
print(postorder(root))

