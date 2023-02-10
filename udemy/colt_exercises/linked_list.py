
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

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next


    def __repr__(self):
        return f"LinkedList: \nhead:{repr(self.head)}, \ntail:{repr(self.tail)}, \nlength:{repr(self.length)}"

l = SinglyLinkedList()
l.push("HI")
l.push("THERE")
l.traverse()
