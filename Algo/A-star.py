import heapq
def a_star(graph, start, goal, heuristic):
    queue = [(0 + heuristic[start], 0, start, [])]
    visited = set()

    while queue:
        g, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]

        if node == goal:
            return path, g

        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (g + cost + heuristic[neighbor], g + cost, neighbor, path))
    return None, float('inf')

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': []
}

heuristic = {'A': 3, 'B': 1, 'C': 1, 'D': 0}
path, cost = a_star(graph, 'A', 'D', heuristic)
print(f"duong di A* : {path}, chi phi: {cost}")
