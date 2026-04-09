tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

visited = []

def dfs(node):
    visited.append(node)
    for neighbor in tree[node]:
        dfs(neighbor)

dfs(1)
print("For DFS:", *visited)