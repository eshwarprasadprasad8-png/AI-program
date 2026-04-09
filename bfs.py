
from collections import deque

tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

def bfs(start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        visited.append(node)
        for neighbor in tree[node]:
            queue.append(neighbor)

    print("For BFS:", *visited)

bfs(1)