"""
BST слева значения меньше, чем родитель
      42
    /   \
  30    50
 /     /  \
21    47   65
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None


tree = BinarySearchTree()
tree.root = Node(10)
tree.root.right = Node(15)
tree.root.left = Node(7)
tree.root.left.right = Node(8)
