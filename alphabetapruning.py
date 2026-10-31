
def alphabeta(node, depth, alpha, beta, maximizing, pruned):

    if depth == 0:
        return node

    if maximizing:
        best = float('-inf')

        for i, child in enumerate(node):
            val = alphabeta(child, depth - 1,
                            alpha, beta, False, pruned)

            best = max(best, val)
            alpha = max(alpha, best)

            if alpha >= beta:
                for x in node[i + 1:]:
                    pruned.extend(x if isinstance(x, list) else [x])
                break

        return best

    else:
        best = float('inf')

        for i, child in enumerate(node):
            val = alphabeta(child, depth - 1,
                            alpha, beta, True, pruned)

            best = min(best, val)
            beta = min(beta, best)

            if alpha >= beta:
                for x in node[i + 1:]:
                    pruned.extend(x if isinstance(x, list) else [x])
                break

        return best


tree = [
    [3, 5, 6],
    [2, 9, 1]
]

pruned = []

result = alphabeta(tree, 2,
                   float('-inf'),
                   float('inf'), True, pruned)

print("Optimal value:", result)
print("Pruned nodes:", pruned)
