#!/usr/bin/env python3
import numpy as np

graph_matrix = (
[0, 1, 0, 1, 0, 0], [1, 0, 1, 0, 0, 1], [0, 1, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 0, 1, 1, 0, 1], [0, 1, 0, 0, 1, 0])
graph_matrix = np.array(graph_matrix)


def search_peaks(i: int, graph_matrix):
    adjacent_peaks = []
    apex_num = len(graph_matrix)
    for k in range(apex_num):
        if graph_matrix[k][i] == 1:
            adjacent_peaks.append(k)
    return adjacent_peaks

def bigSearch(start: int, graph_matrix):
    visited = []
    adjacent_peaks = []
    for i in range(len(graph_matrix)):
        visited.append(False)
    next = start
    while False in visited:
        adjacent_peaks = search_peaks(next, graph_matrix)
        if len(adjacent_peaks) > 1:
            for peak in adjacent_peaks:
                if not visited[peak]:
                   visited.pop(peak)
                   visited.insert(peak, True)
                   print(peak, "is visited")
        else:
            if not visited[adjacent_peaks[0]]:
                visited.pop(adjacent_peaks[0])
                visited.insert(adjacent_peaks[0], True)
        next += 1
    return visited


print(search_peaks(3, graph_matrix))
print(bigSearch(0, graph_matrix))
