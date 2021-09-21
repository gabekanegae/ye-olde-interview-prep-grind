def orderOfLargestPlusSign(n, mines):
    mines = set([tuple(i) for i in mines])
    m = [[int((i, j) not in mines) for j in range(n)] for i in range(n)]

    left = [[m[i][j] for j in range(n)] for i in range(n)]
    right = [[m[i][j] for j in range(n)] for i in range(n)]
    top = [[m[i][j] for j in range(n)] for i in range(n)]
    bottom = [[m[i][j] for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(1, n):
            if m[i][j] == 1:
                left[i][j] += left[i][j-1]

    for i in range(1, n):
        for j in range(n):
            if m[i][j] == 1:
                top[i][j] += top[i-1][j]

    for i in range(n):
        for j in reversed(range(n-1)):
            if m[i][j] == 1:
                right[i][j] += right[i][j+1]

    for i in reversed(range(n-1)):
        for j in range(n):
            if m[i][j] == 1:
                bottom[i][j] += bottom[i+1][j]

    best = [[min([left[i][j], top[i][j], right[i][j], bottom[i][j]]) for j in range(n)] for i in range(n)]
    return max(max(row) for row in best)

n = 5
mines = [[4,2]]
# m = [[1,1,1,1,1],
#      [1,1,1,1,1],
#      [1,1,1,1,1],
#      [1,1,1,1,1],
#      [1,1,0,1,1]]

print(orderOfLargestPlusSign(n, mines)) # 2

n = 10
mines = [[0,1],[0,6],[1,1],[1,3],[1,7],[2,3],
         [2,6],[2,8],[3,0],[3,1],[3,2],[3,3],
         [3,5],[3,6],[3,8],[3,9],[4,3],[5,9],
         [6,1],[6,2],[6,3],[6,5],[6,6],[6,8],
         [7,1],[7,6],[7,7],[8,2],[8,3],[8,5],
         [8,7],[8,8],[9,1],[9,6],[9,8],[9,9]]
# mat = [[1,0,1,1,1,1,0,1,1,1],
#        [1,0,1,0,1,1,1,0,1,1],
#        [1,1,1,0,1,1,0,1,0,1],
#        [0,0,0,0,1,0,0,1,0,0],
#        [1,1,1,0,1,1,1,1,1,1],
#        [1,1,1,1,1,1,1,1,1,0],
#        [1,0,0,0,1,0,0,1,0,1],
#        [1,0,1,1,1,1,0,0,1,1],
#        [1,1,0,0,1,0,1,0,0,1],
#        [1,0,1,1,1,1,0,1,0,0]]

print(orderOfLargestPlusSign(n, mines)) # 5