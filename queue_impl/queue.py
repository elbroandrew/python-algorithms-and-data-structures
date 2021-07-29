class Queue():
    def __init__(self):
        self.items = []

    def add(self, element):
        self.items = [element] + self.items
    
    def pop(self):
        if len(self.items) == 0:
            return 'Nothing to pop.'
        return self.items.pop()

    def show_all(self):
        return self.items

    def peek_next_element(self):
        if len(self.items) == 0:
            return "No elements."
        return self.items[len(self.items)-1]
    
    def is_empty(self):
        return len(self.items) == 0

    def get_size(self):
        return len(self.items)