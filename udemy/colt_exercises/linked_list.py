
"""first create a node"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

first = Node("hi")
first.next = Node("there")
first.next.next = Node("how")
first.next.next.next = Node("are")
first.next.next.next.next = Node("you")