
import heapq

def astar():
    start = (0, 0)
    goal = 2

    pq = [(1, 0, start, [])]
    visited = {}

    while pq:
        f, g, (a, b), path = heapq.heappop(pq)

        if a == goal:
            return path + [(a, b)]

        if (a, b) in visited and visited[(a, b)] <= g:
            continue

        visited[(a, b)] = g

        # Fill, Empty and Transfer operations
        next_states = [
            (4, b), (a, 3),       # Fill
            (0, b), (a, 0),       # Empty
            (a - min(a, 3-b), b + min(a, 3-b)),
            (a + min(b, 4-a), b - min(b, 4-a))
        ]

        for x, y in next_states:
            if (x, y) not in visited:
                cost = g + 1
                h = 0 if x == goal else 1

                heapq.heappush(
                    pq, (cost + h, cost, (x, y),
                         path + [(a, b)])
                )

    return None


result = astar()

print("Solution:")
for state in result:
    print(state)
