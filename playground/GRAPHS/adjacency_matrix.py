"""
better then list in searching of edges
"""

class Node:

    def __init__(self, name):
        self._name = name

class Graph:

    def __init__(self, size: int):
        self.matrix = [[ 0 for _ in range(size) ] for _ in range(size)]

    def add_node(self, node):
        pass

    def add_edge(self, src: int, dst: int) -> None:
        self.matrix[src][dst] = 1

    def check_edge(self, src: int, dst: int) -> bool:
        if self.matrix[src][dst] == 1:
            return True
        return False

    def print_matrix(self):
        for row in self.matrix:
            print(row)

def main():
    g = Graph(5)
    g.add_node(Node('A'))
    g.add_node(Node('B'))
    g.add_node(Node('C'))
    g.add_node(Node('D'))
    g.add_node(Node('E'))

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 0)
    g.add_edge(4, 2)

    g.print_matrix()

if __name__ == '__main__':
    main()