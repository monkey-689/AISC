
def tsp(cost, curr, visited, total, count):
    global ans, path

    n = len(cost)

    if count == n:
        total += cost[curr][0]

        if total < ans:
            ans = total
            path = visited + [0]
        return

    for i in range(n):
        if i not in visited:
            visited.append(i)

            tsp(cost, i, visited,
                total + cost[curr][i], count + 1)

            visited.pop()


cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

ans = float('inf')
path = []

tsp(cost, 0, [0], 0, 1)

print("Minimum cost:", ans)
print("Minimum cost tour:", path)
