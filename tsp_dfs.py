
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = ["A", "B", "C", "D"]
n = len(graph)

best_cost = float("inf")
best_path = []

def dfs(city, visited, path, cost):
    global best_cost, best_path

    # If all cities are visited
    if len(path) == n:

        # Return to starting city A
        total = cost + graph[city][0]
        tour = path + [0]

        print("Tour:", " -> ".join(cities[i] for i in tour),
              "| Cost =", total)

        # Update minimum cost
        if total < best_cost:
            best_cost = total
            best_path = tour

        return

    # Visit every unvisited city
    for nxt in range(n):
        if nxt not in visited:
            dfs(
                nxt,
                visited + [nxt],
                path + [nxt],
                cost + graph[city][nxt]
            )

print("All tours found by DFS:")

dfs(0, [0], [0], 0)

print("\nMinimum cost tour:",
      " -> ".join(cities[i] for i in best_path))

print("Minimum cost:", best_cost)
