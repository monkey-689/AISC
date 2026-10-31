def solve(n, row, board):
    if row == n:
        for r in board:
            print(" ".join("Q" if x else "." for x in r))
        print()
        return True

    for col in range(n):
        safe = True

        for i in range(row):
            if (board[i][col] or
                (row - i == abs(col - board[i].index(1)))):
                safe = False
                break

        if safe:
            board[row][col] = 1

            if solve(n, row + 1, board):
                return True

            board[row][col] = 0

    return False


n = int(input("Enter N : "))
board = [[0] * n for _ in range(n)]

if not solve(n, 0, board):
    print("No solution")
