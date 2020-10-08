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

print(search_peaks(3, graph_matrix))