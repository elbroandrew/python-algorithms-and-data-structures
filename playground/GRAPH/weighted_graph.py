

class PriorityQueue:
    def __init__(self):
        self.values = []

    def sort(self):
        self.values.sort(key=lambda x: x['priority'])  #  sort dicts inside the list by priority

    def enqueue(self, val, priority):
        self.values.append(dict(val=val, priority=priority))
        self.sort()

    def dequeue(self):
        return self.values.pop(0)




class WeightedGraph:

    def __init__(self):
        self.adj_list = {}


    def add_vertex(self, vertex):
        if not vertex in self.adj_list.keys():
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        self.adj_list[vertex1].append(dict(node=vertex2, weight=weight))
        self.adj_list[vertex2].append(dict(node=vertex1, weight=weight))


def main():
    q = PriorityQueue()
    q.enqueue("B", 3)
    q.enqueue("C", 5)
    q.enqueue("D", 2)
    q.enqueue("Q", 20)
    print(q.values)


if __name__ == '__main__':
    main()