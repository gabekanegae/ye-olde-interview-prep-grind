from collections import deque

def pacificAtlantic(matrix):
    if not matrix: return []

    r, c = len(matrix), len(matrix[0])
    topLeft = set([(i, 0) for i in range(r)] + [(0, i) for i in range(c)])
    bottomRight = set([(i, c-1) for i in range(r)] + [(r-1, i) for i in range(c)])

    def reaches(x, y, goal):
        queue = deque([(x, y)])
        visited = set()
        while queue:
            curX, curY = queue.popleft()
            
            if (curX, curY) in goal:
                return True

            visited.add((curX, curY))

            for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                nxtX, nxtY = curX+dx, curY+dy
                if not (0 <= nxtX < r and 0 <= nxtY < c): continue
                if (nxtX, nxtY) in visited: continue

                if matrix[nxtX][nxtY] <= matrix[curX][curY]:
                    queue.append((nxtX, nxtY))

        return False

    for i in range(r):
        for j in range(c):
            if reaches(i, j, topLeft):
                topLeft.add((i, j))
            if reaches(i, j, bottomRight):
                bottomRight.add((i, j))

    return [[i, j] for i, j in topLeft.intersection(bottomRight)]

print(pacificAtlantic([[1, 2, 2, 3, 5],
                       [3, 2, 3, 4, 4],
                       [2, 4, 5, 3, 1],
                       [6, 7, 1, 4, 5],
                       [5, 1, 1, 2, 4]]))