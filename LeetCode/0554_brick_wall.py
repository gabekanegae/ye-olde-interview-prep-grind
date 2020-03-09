def leastBricks(wall):
    for bricks in wall:
        accSum = 0
        for i in range(len(bricks)):
            accSum += bricks[i]
            bricks[i] = accSum

    counts = dict()
    for bricks in wall:
        for b in bricks[:-1]:
            if b not in counts:
                counts[b] = 0
            counts[b] += 1

    if not counts: return len(wall)
    return len(wall) - max(counts.values())

print(leastBricks([[1,2,2,1], [3,1,2], [1,3,2], [2,4], [3,1,2], [1,3,1,1]]))
print(leastBricks([[1], [1], [1]]))