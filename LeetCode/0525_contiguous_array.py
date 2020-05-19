def findMaxLength(nums):
    cur = 0
    seen = dict()
    best = 0
    for i, n in enumerate(nums):
        if cur not in seen:
            seen[cur] = i

        if n == 0: cur -= 1
        elif n == 1: cur += 1

        if cur in seen:
            best = max(best, i - seen[cur] + 1)

    return best

print(findMaxLength([0, 1, 1, 0, 1])) # 4