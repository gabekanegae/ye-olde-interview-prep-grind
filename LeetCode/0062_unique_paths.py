def uniquePaths(m, n):
    memo = {(0, 0): 1}

    def rec(i, j):
        if i < 0 or j < 0: return 0
        if (i, j) in memo: return memo[(i, j)]

        memo[(i, j)] = rec(i-1, j) + rec(i, j-1)
        return memo[(i, j)]

    return rec(m-1, n-1)

print(uniquePaths(7, 3))
print(uniquePaths(23, 12))