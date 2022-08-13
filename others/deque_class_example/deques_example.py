

class MyDeque:
    

    def __init__(self):
        self.arr = []

    
    # push back
    def push_back(self, element):
        self.arr.append(element)

    # push front
    def push_front(self, element):
        self.arr.insert(0, element)
        print(self.arr)

    # pop back
    def pop_back(self):
        if len(self.arr) != 0:
            self.arr.pop()
        else:
            raise Exception("Deque shouldn't be empty.")


    # pop front
    def pop_front(self):
        if len(self.arr) != 0:
            self.arr = self.arr[1::]
        else:
            raise Exception("Deque shouldn't be empty.")


    # is empty
    def is_empty(self):
        return len(self.arr) == 0

    # clear
    def clear(self):
        self.arr.clear()

    # deque size
    def show(self):
        print(self.arr)
