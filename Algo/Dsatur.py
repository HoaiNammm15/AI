def dsatur(graph):
    colors = {}
    saturation = {node: 0 for node in graph}
    degrees = {node: len(neighs) for node, neighs in graph.items()}
    
    while len(colors) < len(graph):
        uncolored = [node for node in graph if node not in colors]
        node = max(uncolored, key=lambda x: (saturation[x], degrees[x]))

        used_colors = {colors.get(neigh) for neigh in graph[node] if neigh in colors}
        color = 0
        while color in used_colors:
            color += 1
        colors[node] = color

        for neigh in graph[node]:
            if neigh not in colors:
                saturation[neigh] = len({colors.get(n) for n in graph[neigh] if n in colors})

    return colors

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

coloring = dsatur(graph)
print("To mau:", coloring)
