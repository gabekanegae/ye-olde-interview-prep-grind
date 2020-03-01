def checkValid(value, tr, tc, board):
    for r in range(9):
        if r == tr: continue
        if board[r][tc] == value: return False

    for c in range(9):
        if c == tc: continue
        if board[tr][c] == value: return False

    subtr, subtc = (tr//3)*3, (tc//3)*3
    for r in range(3):
        for c in range(3):
            if (r, c) == (tr, tc): continue
            if board[subtr+r][subtc+c] == value: return False

    return True

def solve(board, r=0, c=0):
    if c == 9:
        r, c = r+1, 0
        if r == 9:
            return True

    if board[r][c] != 0:
        return solve(board, r, c+1)

    for value in range(1, 9+1):
        if checkValid(value, r, c, board):
            board[r][c] = value
            
            if solve(board, r, c+1):
                return True

            board[r][c] = 0

    return False

board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

solve(board)

print("\n".join([" ".join([str(c) for c in row]) for row in board]))