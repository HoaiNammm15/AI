import heapq

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

def get_neighbors(state):
    neighbors = []
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def is_goal(state):
    return state == goal_state

def serialize(state):
    return str(state)

def gt1_ucs(start):
    heap = [(0, start, [])]
    visited = set()

    while heap:
        cost, current, path = heapq.heappop(heap)
        key = serialize(current)
        if key in visited:
            continue
        visited.add(key)

        if is_goal(current):
            return path + [current]

        for neighbor in get_neighbors(current):
            heapq.heappush(heap, (cost + 1, neighbor, path + [current]))

    return None
