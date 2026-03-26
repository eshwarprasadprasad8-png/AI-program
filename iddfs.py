tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

def dls(tree, node, depth, visited):
    if depth < 0:
        return
    visited.append(node)
    if depth == 0:
        return
    for neighbor in tree[node]:
        dls(tree, neighbor, depth - 1, visited)

def iddfs(tree, start, max_depth):
    for depth in range(max_depth + 1):
        visited = []
        dls(tree, start, depth, visited)
        print("Depth", depth, ":", visited)

iddfs(tree, 1, 2)