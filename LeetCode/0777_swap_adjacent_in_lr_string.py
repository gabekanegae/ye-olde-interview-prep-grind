def canTransform1(start, end):
    startX = "".join([c for c in start if c != "X"])
    endX = "".join([c for c in end if c != "X"])    

    if startX != endX: return False

    startR = [i for i in range(len(start)) if start[i] == "R"]
    startL = [i for i in range(len(start)) if start[i] == "L"]
    endR = [i for i in range(len(end)) if end[i] == "R"]
    endL = [i for i in range(len(end)) if end[i] == "L"]

    for s, e in zip(startR, endR):
        if s > e: return False

    for s, e in zip(startL, endL):
        if s < e: return False

    return True

def canTransform2(start, end):
    n = len(start)
    i, j = 0, 0

    while i < n or j < n:
        while i < n and start[i] == "X": i += 1
        while j < n and end[j] == "X": j += 1

        if (i < n) != (j < n): return False

        if i < n and j < n:
            if (start[i] != end[j]) or (start[i] == "L" and i < j) or (end[j] == "R" and i > j):
                return False

        i += 1
        j += 1

    return True

print(canTransform1("RXXLRXRXL", "XRLXXRRLX")) # True
print(canTransform2("RXXLRXRXL", "XRLXXRRLX")) # True

print(canTransform1("XXXXXLXXXX", "LXXXXXXXXX")) # True
print(canTransform2("XXXXXLXXXX", "LXXXXXXXXX")) # True

print(canTransform1("RXR", "XXR")) # False
print(canTransform2("RXR", "XXR")) # False