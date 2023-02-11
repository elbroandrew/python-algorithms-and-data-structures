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

    def __repr__(self):
        return f"\n[Node: value:{self.value}, left node -> {self.left}, right node -> {self.right}]"



class BinarySearchTree:

    def __init__(self):
        self.root = None


    def insert(self, val):
        n = Node(val)
        if not self.root:
            self.root = n
            return
        current_node = self.root
        while True:
            # выйти если дубликат
            if val == current_node.value:
                return
            # если значение, которое ищу меньше, то налево
            if current_node.value > n.value:
                if not current_node.left:
                    current_node.left = n
                    return
                current_node = current_node.left
            # ищу справа
            elif current_node.value < n.value:
                if not current_node.right:
                    current_node.right = n
                    return
                current_node = current_node.right


    def __str__(self):
        return f"Binary tree: \nRoot:{self.root}"




tree = BinarySearchTree()
tree.root = Node(10)
tree.insert(7)
tree.insert(15)
tree.insert(11)
tree.insert(16)
tree.insert(16)
print(tree)
