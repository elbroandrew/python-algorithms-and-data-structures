from binary_search_tree import *

"""PRE-ORDER SOLUTION"""

t = BinarySearchTree()
t.insert(10)
t.insert(6)
t.insert(3)
t.insert(8)
t.insert(15)
t.insert(20)

def dfs_pre_order(b: BinarySearchTree):
    data = []
    def traverse(node: Node):
        data.append(node.value)
        if node.left:
            traverse(node.left)
        if node.right:
            traverse(node.right)
    traverse(b.root)
    return data

print(dfs_pre_order(t))
