from collections import deque

moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    m = len(grid[0])

    start = (0, 0)
    end = (n-1, m-1)

    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return -1

    queue = deque([(start, 1)])
    visited = set()
    while queue:
        cur, dist = queue.popleft()

        if cur in visited: continue
        visited.add(cur)

        if cur == end:
            return dist

        for delta in moves:
            nxt = (cur[0]+delta[0], cur[1]+delta[1])

            if 0 <= nxt[0] < n and 0 <= nxt[1] < m and grid[nxt[0]][nxt[1]] == 0:
                queue.append((nxt, dist+1))

    return -1

print(shortestPathBinaryMatrix([[0, 1],
                                [1, 0]])) # 2

print(shortestPathBinaryMatrix([[0, 0, 0],
                                [1, 1, 0],
                                [1, 1, 0]])) # 4


print(shortestPathBinaryMatrix([[1, 0, 0],
                                [1, 1, 0],
                                [1, 1, 0]])) # -1


print(shortestPathBinaryMatrix([[0, 0, 0, 0, 1],
                                [1, 0, 0, 0, 0],
                                [0, 1, 0, 1, 0],
                                [0, 0, 0, 1, 1],
                                [0, 0, 0, 1, 0]])) # -1