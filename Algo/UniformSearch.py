import heapq
def uniform_cost_search(graph, start, goal):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        path = path + [node]
        visited.add(node)

        if node == goal:
            return path, cost

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))

    return None, float("inf")
graph = {
    'A': [('B', 1), ('C', 5)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}
path, cost = uniform_cost_search(graph, 'A', 'D')
print(f"Duong di: {path}, CHi phi: {cost}")
