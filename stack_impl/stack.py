class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def top(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items)-1]
    
    def getSize(self):
        return len(self.items)

    def is_empty(self) -> bool:
        return len(self.items) == 0

    




