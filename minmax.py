
def minimax(node, depth, maximizing):

    if depth == 0:
        return node

    if maximizing:
        best = float('-inf')

        for child in node:
            val = minimax(child, depth - 1, False)
            best = max(best, val)

        return best

    else:
        best = float('inf')

        for child in node:
            val = minimax(child, depth - 1, True)
            best = min(best, val)

        return best


tree = [
    [3, 5, 6],
    [2, 9, 1]
]

result = minimax(tree, 2, True)

print("Optimal value:", result)
