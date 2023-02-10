
"""a linked list should have a length, a head and a tail"""

"""first create a node"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"Node:\n value:{repr(self.val)}, next -> {self.next}"


"""second create an interface called list"""
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        n = Node(val)
        if not self.head:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

        self.length += 1

    def pop(self):
        if not self.head:
            return
        current_node = self.head
        new_tail = current_node
        while current_node.next:
            new_tail = current_node
            current_node = current_node.next
        self.tail = new_tail
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current_node

    def shift(self):
        if not self.head:
            return

        old_head = self.head
        self.head = old_head.next
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return old_head


    def __repr__(self):
        return f"LinkedList: \nhead:{repr(self.head)}, \ntail:{repr(self.tail)}, \nlength:{repr(self.length)}"

l = SinglyLinkedList()
l.push("HI")
l.push("WORLD")
print(l)
print(l.shift())
print(l)
print(l.shift())
print(l)
