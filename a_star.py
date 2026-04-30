import heapq
goal_state = [[1,2,3],
              [4,5,6],
              [7,8,0]]
moves = [(-1,0,"Up"), (1,0,"Down"), (0,-1,"Left"), (0,1,"Right")]
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def heuristic(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x = (val - 1) // 3
                goal_y = (val - 1) % 3
                dist += abs(i - goal_x) + abs(j - goal_y)
    return dist
def to_tuple(state):
    return tuple(tuple(row) for row in state)

# Generate next states
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    for dx, dy, move in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append((new_state, move))
    return neighbors
def a_star(start):
    pq = []
    heapq.heappush(pq, (0, start, []))
    visited = set()

    while pq:
        cost, current, path = heapq.heappop(pq)

        if current == goal_state:
            return path + [current]

        visited.add(to_tuple(current))

        for neighbor, move in get_neighbors(current):
            if to_tuple(neighbor) not in visited:
                new_cost = len(path) + 1 + heuristic(neighbor)
                heapq.heappush(pq, (new_cost, neighbor, path + [current]))

    return None

# Print solution
def print_solution(solution):
    for step, state in enumerate(solution):
        print(f"\nStep {step}:")
        for row in state:
            print(row)

start_state = [[1,2,3],
               [4,0,6],
               [7,5,8]]
solution = a_star(start_state)

if solution:
    print("Solution Found!")
    print_solution(solution)
else:
    print("No Solution Found")