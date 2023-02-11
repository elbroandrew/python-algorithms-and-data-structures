
"""a linked list should have a length, a head and a tail"""

"""
Big O:
insert -> O(1)
get -> O(N)
remove - depends O(1) or O(N)
"""

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
        return True

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

    def unshift(self, val):
        n = Node(val)
        if not self.head:
            self.head = n
            self.tail = self.head
        else:
            n.next = self.head
            self.head = n
        self.length += 1
        return True

    def get(self, idx):
        """get node"""
        if not self.head:
            return None
        if idx < 0 or idx >= self.length:
            return None
        count = 0
        result = self.head
        while count < idx:
            result = result.next
            count += 1
        return result


    def set(self, val, at_index):
        """updates a node at the index"""
        if x := self.get(at_index):
            x.val = val
            return True

        return False


    def insert(self, val, idx):

        """inserts a new node"""
        if idx < 0 or idx > self.length:
            return False
        elif idx == self.length:
            return self.push(val)
        elif idx == 0:
            return self.unshift(val)

        new_node = Node(val)
        prev_node = self.get(idx - 1)
        prev_node_next = prev_node.next
        prev_node.next = new_node
        new_node.next = prev_node_next
        self.length += 1

        return True

    def remove(self, at_index):
        if at_index < 0 or at_index >= self.length:
            return None
        elif at_index == 0:
            self.shift()
        elif at_index == self.length - 1:
            self.pop()
        prev_node = self.get(at_index - 1)
        removed_node = self.get(at_index)
        removed_node_next = removed_node.next
        prev_node.next = removed_node_next
        self.length -= 1

        return removed_node

    def reverse(self):
        # swap head and tail
        current_node = self.head
        self.head = self.tail
        self.tail = current_node

        # loop through the list
        next_node = None
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return self



    def __repr__(self):
        return f"LinkedList: \nhead:{repr(self.head)}, \ntail:{repr(self.tail)}, \nlength:{repr(self.length)}"

l = SinglyLinkedList()

l.insert("hi", 0)
l.push(1)
l.push(2)
l.push(3)
l.push(4)
print(l)
l.reverse()
print("-----------------")
print(l)