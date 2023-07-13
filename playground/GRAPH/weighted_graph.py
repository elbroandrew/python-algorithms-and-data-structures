class WeightedGraph:

    def __init__(self):
        self.adj_list = {}


    def add_vertex(self, vertex):
        if not vertex in self.adj_list.keys():
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        self.adj_list[vertex1].append(dict(node=vertex2, weight=weight))
        self.adj_list[vertex2].append(dict(node=vertex1, weight=weight))


