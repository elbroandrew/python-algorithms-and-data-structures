"""
list (not dict) implementation
"""

class Node:

    def __init__(self, data):
        self.data = data



class Graph:

    def __init__(self):
        self._alist = []


    def add_node(self, node: Node):
        self._alist.append([node])

    def add_edge(self, src, dst):
        cur_list = self._alist[src]
        dst_node = self._alist[dst][0]
        cur_list.append(dst_node)

    def check_edge(self, src: int, dst: int) -> bool:
        cur_list = self._alist[src]
        dst_node = self._alist[dst][0]

        for n in cur_list:
            if n == dst_node:
                return True

        return False

    def print_graph(self):

        for cur_list in self._alist:
            for node in cur_list:
                print("%s -> " % node.data, end='')
            print("")


def main():
    g = Graph()
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

    g.print_graph()




if __name__ == '__main__':
    main()