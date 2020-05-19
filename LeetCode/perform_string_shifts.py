def stringShift(s, shift):
    shiftLeft = 0
    for direction, amt in shift:
        if direction == 0: # left
            shiftLeft += amt
        elif direction == 1: # right
            shiftLeft -= amt

    shiftLeft %= len(s)
    return "".join(s[shiftLeft:] + s[:shiftLeft])

# "efgabcd"
print(stringShift("abcdefg",
                  [[1,1],[1,1],[0,2],[1,3]]))

# "qpifxqgwki"
print(stringShift("xqgwkiqpif",
                  [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]))