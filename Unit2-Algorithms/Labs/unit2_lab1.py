# Lab 1 - Traversing Binary Trees


# Task 1 - Implement a Binary Tree Node
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None 
    
    # Task 4 - Implement Insertion pt.1
    def insert(self, node):
        if node.val < self.val:
            # If there isnt already a node on that branch add the node
            if not self.left:
                self.left = node
            # Else, move down to the next node and recurr
            else:
                self.left.insert(node)
        elif node.val > self.val:
            if not self.right:
                self.right = node
            else:
                self.right.insert(node)
        else:
            pass

    # Task 3 - Implement Preorder, Inorder, and Postorder Traversals pt.1
    def print_preorder(self):
        # The root node is visited first, followed by the left child nodes, then the right child nodes.
        print(self.val, end=" ")
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()
    
    def print_inorder(self):
        # Left leaf node is visited first then the parent node and then the right node 
        if self.left:
            # Call recursivly untill leaf node is reached
            self.left.print_inorder()
        print(self.val, end=" ")
        if self.right:
            self.right.print_inorder()

    def print_postorder(self):
        # The left child is visited first, followed by the right child, then the root node.
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print(self.val, end=" ")


# !! A different insert function outside of the Node class !!
# def insert_outside(root, new_node):
#     if not root:
#         return new_node
#     if new_node.val < root.val:
#         root.left = insert_outside(root.left, new_node)
#     elif new_node.val > root.val:
#         root.right = insert_outside(root.right, new_node)
#     return root


# Task 2 - Build a Binary Tree (BEFORE ADDING INSERTIONS)
# root = Node(3)
# root.left = Node(1)
# root.right = Node(4)
# root.left.right = Node(2)

# Task 2 - Build a Binary Tree (AFTER ADDING INSERTIONS)
root = Node(3)
root.insert(Node(1))
root.insert(Node(2))
root.insert(Node(4))


# Task 3 - Implement Preorder, Inorder, and Postorder Traversals pt.2
print("\nPreorder")
root.print_preorder()
print()

print("\nInorder")
root.print_inorder()
print()

print("\nPostorder")
root.print_postorder()
print()


# Task 4 - Implement Insertion pt.2
root.insert(Node(5))
root.insert(Node(0))

# Testing insertions
print("\nInorder (after insertions):")
root.print_inorder()
print("\n")

# !! Only for the insert_outside function outside of the class !!
# root = insert_outside(root, Node(6))
# print("\nInorder (after insertions pt.2):")
# root.print_inorder()
# print("\n")
