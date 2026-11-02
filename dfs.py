
def dfs(graph, node, visited):

    visited.add(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


graph = {
    'P': ['Q', 'R'],
    'Q': ['S', 'T'],
    'R': ['U', 'V'],
    'S': [],
    'T': [],
    'U': [],
    'V': []
}

visited = set()

print("DFS Traversal:")
dfs(graph, 'P', visited)
