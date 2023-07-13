"""
Graph traversal use cases
1. peer to peer networking
2. web crawlers
3. find closest matches
4. shortest paths:
-- AI path in games
-- solving mazes
-- GPS navigation
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

    print("======TRAVERSE======")

    traversed_list = g.dfs_recursive_traverse(g.root)
    print(traversed_list)


"""
//          A
//        /   \
//       B     C
//       |     |
//       D --- E
//        \   /
//          F
"""

if __name__ == '__main__':
    main()

