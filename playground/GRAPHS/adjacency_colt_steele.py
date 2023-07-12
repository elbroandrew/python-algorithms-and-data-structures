## -*- coding: utf-8 -*-
"""
FOR undirected graph
2 способа хранения графа:
- adjacency matrix
- adjacency list

matrix: просто в таблице показываем какие есть между какими вершинами рёбра.

   | A | B | C | D |
--------------------
A | 0 | 1 | 0 | 1 |
B | 1 | 0 | 0 | 0 |
C | 0 | 0 | 1 | 1 |
D | 0 | 1 | 1 | 0 |

list:
каждый элемент списка - это номер вершины, и каждой соответствует список с какими вершинами она связан
graph:

    0
  /  \
 1    3
  \ /
   2
    \
     4

[
 [1, 3],
 [0, 2],
 [1, 3, 4],
 [0, 2],
 [2]
]

или словарь
{
 "A":[1,3],
 "B":[0,2]
 ......
}


матрица быстрее ищет рёбра.
Остальное хуже, чему у списка.
"""

class UndirectedGraph:
    def __init__(self):
        self._adjacency_list = dict()


    def get_vertices(self):
        return self._adjacency_list

    def add_vertex(self, vertex):
        if not vertex in self._adjacency_list.keys():
            self._adjacency_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 in self._adjacency_list.keys():
            if not v2 in self._adjacency_list[v1]:
                self._adjacency_list[v1].append(v2)
        else:
            self.add_vertex(v1)
            self._adjacency_list[v1].append(v2)

        if v2 in self._adjacency_list.keys():
            if not v1 in self._adjacency_list[v2]:
                self._adjacency_list[v2].append(v1)
        else:
            self.add_vertex(v2)
            self._adjacency_list[v2].append(v1)

    def remove_edge(self, v1, v2):
        # if v2 in self._adjacency_list[v1]:
        #     self._adjacency_list[v1].remove(v2)
        # if v1 in self._adjacency_list[v2]:
        #     self._adjacency_list[v2].remove(v1)

        # FILTER
        self._adjacency_list[v1] = list(filter(lambda vertex: vertex != v2, self._adjacency_list[v1]))
        self._adjacency_list[v2] = list(filter(lambda vertex: vertex != v1, self._adjacency_list[v2]))

    def remove_vertex(self, vertex):
        while len(self._adjacency_list) > 0:
            removed_vertex = self._adjacency_list[vertex].pop()
            self.remove_edge(vertex, removed_vertex)

        self._adjacency_list.pop(vertex)




g = UndirectedGraph()
g.add_vertex("Tokyo")
g.add_vertex("Dallas")
g.add_vertex("Aspen")
print(g.get_vertices())
g.add_edge("Tokyo", "Dallas")
print(g.get_vertices())
g.add_edge("Dallas", "Aspen")
print(g.get_vertices())

