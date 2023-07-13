"""
BFS is used in A*
"""

from playground.GRAPH.adjacency_colt_steele import UndirectedGraph


def main():
    g = UndirectedGraph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "E")
    g.add_edge("D", "E")
    g.add_edge("D", "F")
    g.add_edge("E", "F")
    print(g.get_vertices())

    r = g.bfs(g.root)
    print(r)



if __name__ == '__main__':
    main()