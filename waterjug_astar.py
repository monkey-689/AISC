
import heapq

def astar():

    # Initial state: both jugs are empty
    jug1 = 0
    jug2 = 0

    # Goal: get 2 litres in either jug
    goal = 2

    # Priority queue: (f, g, state, path)
    queue = [(1, 0, (jug1, jug2), [])]

    visited = {}

    while queue:

        # Get the state with the lowest f value
        f, cost, state, path = heapq.heappop(queue)

        jug1, jug2 = state

        # Check whether goal is reached
        if jug1 == goal:
            return path + [(jug1, jug2)]

        # Skip already visited states with lower cost
        if state in visited and visited[state] <= cost:
            continue

        visited[state] = cost

        # Generate possible next states

        next_states = [

            (4, jug2),  # Fill jug1
            (jug1, 3),  # Fill jug2

            (0, jug2),  # Empty jug1
            (jug1, 0),  # Empty jug2

            # Pour jug1 into jug2
            (
                jug1 - min(jug1, 3 - jug2),
                jug2 + min(jug1, 3 - jug2)
            ),

            # Pour jug2 into jug1
            (
                jug1 + min(jug2, 4 - jug1),
                jug2 - min(jug2, 4 - jug1)
            )
        ]

        # Add next states to priority queue
        for new_jug1, new_jug2 in next_states:

            new_state = (new_jug1, new_jug2)

            if new_state not in visited:

                new_cost = cost + 1

                # Simple heuristic
                heuristic = 0 if new_jug1 == goal else 1

                total_cost = new_cost + heuristic

                heapq.heappush(
                    queue,
                    (
                        total_cost,
                        new_cost,
                        new_state,
                        path + [state]
                    )
                )

    return None


result = astar()

print("Solution:")

for state in result:
    print(state)
