
from collections import deque

def bfs(n):
    q = deque([[]])

    while q:
        s = q.popleft()
        row = len(s)

        if row == n:
            return s

        for col in range(n):
            safe = True

            for r in range(row):
                if (s[r] == col or
                    abs(s[r] - col) == abs(r - row)):
                    safe = False
                    break

            if safe:
                q.append(s + [col])

    return None


n = int(input("Enter N (4 or 8): "))
ans = bfs(n)

if ans:
    for r in range(n):
        for c in range(n):
            if ans[r] == c:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution")
