def floodFill(image, sr, sc, newColor):
    if image[sr][sc] == newColor: return image

    origColor = image[sr][sc]

    def rec(r, c):
        if not (0 <= r < len(image) and 0 <= c < len(image[0])):
            return

        if image[r][c] != origColor:
            return

        image[r][c] = newColor

        rec(r+1, c)
        rec(r-1, c)
        rec(r, c+1)
        rec(r, c-1)

    rec(sr, sc)
    return image

print(floodFill([[1, 1, 1],
                 [1, 1, 0],
                 [1, 0, 1]], 1, 1, 2))

               # [[2, 2, 2],
               #  [2, 2, 0],
               #  [2, 0, 1]])

print(floodFill([[0, 0, 0],
                 [0, 1, 1]], 1, 1, 1))