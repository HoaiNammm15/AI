from Gts1 import is_goal, get_neighbors, serialize
import heapq
def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = divmod(value - 1, 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

def gt2_astar(start):
    heap = [(manhattan(start), 0, start, [])]
    visited = set()

    while heap:
        f, g, current, path = heapq.heappop(heap)
        key = serialize(current)
        if key in visited:
            continue
        visited.add(key)

        if is_goal(current):
            return path + [current]

        for neighbor in get_neighbors(current):
            if serialize(neighbor) not in visited:
                heapq.heappush(heap, (g + 1 + manhattan(neighbor), g + 1, neighbor, path + [current]))

    return None
