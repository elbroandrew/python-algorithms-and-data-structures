## -*- coding: utf-8 -*-

from binary_search_tree import *


t = BinarySearchTree()
t.insert(10)
t.insert(6)
t.insert(3)
t.insert(8)
t.insert(15)
t.insert(20)


"""PRE-ORDER SOLUTION"""

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

print("PRE order solution: %s" % dfs_pre_order(t) )  # PRE order solution: [10, 6, 3, 8, 15, 20]

"""POST-ORDER SOLUTION"""

def dfs_post_order(b:BinarySearchTree):
    visited = []

    def traverse(node: Node):
        if node.left:
            traverse(node.left)
        if node.right:
            traverse(node.right)
        visited.append(node.value)

    traverse(b.root)

    return visited

print("POST order solution: %s" % dfs_post_order(t) )  # POST order solution: [3, 8, 6, 20, 15, 10]

"""IN-ORDER SOLUTION"""
#короче всегда сначала левое поддерево, потом правое. Если нет левого, то сразу записываю родителя и иду в правое"""
'''
Пример:
    10
   /  \
  6    12
 / \     \
3   5     20
правое поддерево (12-20) не имеет левой ветки, значит будет 12-20, а не 20-12.
'''

def dfs_in_order(b:BinarySearchTree):
    visited = []

    def traverse(node: Node):
        if node.left:
            traverse(node.left)
        visited.append(node.value)  # просто сюда переместили аппенд
        if node.right:
            traverse(node.right)

    traverse(b.root)

    return visited

print("IN order solution: %s" % dfs_in_order(t) )  # IN order solution: [3, 8, 6, 20, 15, 10]