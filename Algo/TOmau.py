def greedy_coloring(graph):
    result = {}
    for node in sorted(graph):
        neighbor_colors = {result.get(neigh) for neigh in graph[node] if neigh in result}
        color = 0
        while color in neighbor_colors:
            color += 1
        result[node] = color
    return result

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

coloring = greedy_coloring(graph)
print("To mau:", coloring)
