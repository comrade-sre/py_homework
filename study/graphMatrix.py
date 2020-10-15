#!/usr/bin/env python3
import numpy as np

graph_matrix = (
[0, 1, 0, 1, 0, 0], [1, 0, 1, 0, 0, 1], [0, 1, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 0, 1, 1, 0, 1], [0, 1, 0, 0, 1, 0])
graph_matrix = np.array(graph_matrix)


def search_vertexes(i: int, graph_matrix):
    adjacent_vertexes = []
    apex_num = len(graph_matrix)
    for k in range(apex_num):
        if graph_matrix[k][i] == 1:
            adjacent_vertexes.append(k)
    return adjacent_vertexes

def bigSearch(start: int, graph_matrix):
    visited = []
    adjacent_vertexes = []
    for i in range(len(graph_matrix)):
        visited.append(False)
    next = start
    while False in visited:
        adjacent_vertexes = search_vertexes(next, graph_matrix)
        if len(adjacent_vertexes) > 1:
            for vertex in adjacent_vertexes:
                if not visited[vertex]:
                   visited.pop(vertex)
                   visited.insert(vertex, True)
                   print(vertex, "is visited")
        else:
            if not visited[adjacent_vertexes[0]]:
                visited.pop(adjacent_vertexes[0])
                visited.insert(adjacent_vertexes[0], True)
        next += 1
    return visited


print(search_vertexes(3, graph_matrix))
print(bigSearch(0, graph_matrix))
