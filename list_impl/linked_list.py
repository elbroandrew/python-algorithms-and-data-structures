class Node:
    def __init__(self, value, next_node=None):
        self.index = 0
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.count = 0
        if head is not None:
            self.count = 1

    def print_list(self):
        node = self.head
        while node is not None:
            print(node)
            node = node.next_node


    def get_size(self):
        return self.count

    def index(self, index):
        if self.head is None:
            return f"List is empty"
        else:
            node = self.head
            current_index = 0
            while current_index != index:
                node = node.next_node
                current_index += 1
            return node.value

    def insert(self, node: Node):
        #TOOD: insert at index, etc
        self.count += 1
        self.head.next_node = node

    def erase(self):
        self.count = 0
        self.head = None
