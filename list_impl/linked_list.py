class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, node=None):
        self.node = node

    def get_size(self):
        count = 0
        node = self.node
        while node is not None:
            count += 1
            node = node.next_node

        return count


    def insert(self, node: Node):
        self.node.next_node = node

    def erase(self):
        self.node = None
