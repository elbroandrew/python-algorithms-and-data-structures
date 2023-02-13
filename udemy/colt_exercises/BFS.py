"""
С каждого уровня добавляю в список элементы
------>   10
        /   \
----> 4     20
     / \      \
-> 2    6      33
результат: [10, 4, 20, 2, 6, 33], т.е. слева направо иду по каждому уровню.
"""

import binary_search_tree

"""можно создать либо свою очередь, либо использовать список и pop, """
class Queue:

    def __init__(self):
        self._arr = []
        self.length = 0

    def add(self, val):
        self._arr.append(val)
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



if __name__ == '__main__':
    q = Queue()
    q.add(10)
    q.add(4)
    q.add(12)
    print(q.show())