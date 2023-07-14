

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

    def dijkstra(self, start, finish):
        nodes = PriorityQueue()
        distances = {}
        previous = {}
        path = []
        smallest = None

        # build initial distances state
        for vertex in self.adj_list.keys():
            if vertex == start:
                distances[vertex] = 0
                nodes.enqueue(vertex, 0)
            else:
                distances[vertex] = float('inf')    # use infinity
                nodes.enqueue(vertex, float('inf'))
            previous[vertex] = None

        # as long as there is sth to visit
        while nodes.values:
            smallest = nodes.dequeue()['val']
            print(smallest)
            if smallest == finish:
                # we are done
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]
                break
            if smallest or distances[smallest] != float('inf'):
                for next_node in self.adj_list[smallest]:
                    # calc distance
                    candidate = distances[smallest] + next_node['weight']
                    next_neighbor = next_node['node']
                    if candidate < distances[next_neighbor]:
                        # update new smallest distance to neighbor
                        distances[next_neighbor] = candidate
                        previous[next_neighbor] = smallest
                        nodes.enqueue(next_neighbor, candidate)

        path.append(smallest)
        return [*reversed(path)]



def main():
    graph = WeightedGraph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")

    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "E", 3)
    graph.add_edge("C", "D", 2)
    graph.add_edge("C", "F", 4)
    graph.add_edge("D", "E", 3)
    graph.add_edge("D", "F", 1)
    graph.add_edge("E", "F", 1)

    res = graph.dijkstra("A", "E")
    print(res)

if __name__ == '__main__':
    main()