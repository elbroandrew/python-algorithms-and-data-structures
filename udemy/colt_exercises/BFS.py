from binary_search_tree import *

"""
С каждого уровня добавляю в список элементы
------>   10
        /   \
----> 4     20
     / \      \
-> 2    6      33
результат: [10, 4, 20, 2, 6, 33], т.е. слева направо иду по каждому уровню.
"""

"""можно создать либо свою очередь, либо использовать список и pop, """
class Queue:

    def __init__(self):
        self._arr = []
        self.length = 0

    def add(self, val):
        if self.length == 0:
            self._arr.append(val)
        else:
            self._arr.insert(0, val)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        res = self._arr[-1]
        self._arr = self._arr[:-1]
        self.length -= 1
        return res

    def show(self):
        print(f"{[i for i in self._arr]}")

# breadth first search
def bfs(bst: BinarySearchTree):

    q = Queue()
    if not bst.root:
        return
    q.add(bst.root)
    visited = []

    while q.length > 0:
        v: Node = q.pop()
        visited.append(v.value)
        if v.left:
            q.add(v.left)
        if v.right:
            q.add(v.right)

    return visited


if __name__ == '__main__':
    b = BinarySearchTree()
    b.insert(10)
    b.insert(6)
    b.insert(3)
    b.insert(8)
    b.insert(15)
    b.insert(20)
    b_bfs = bfs(b)
    print(b_bfs)