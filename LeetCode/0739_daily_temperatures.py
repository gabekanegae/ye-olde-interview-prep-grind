def dailyTemperatures(T):
    output = [0 for _ in T]

    seen = []
    for i in range(len(T)-1, -1, -1):
        while seen and seen[-1][0] <= T[i]:
            seen.pop()
        if seen:
            output[i] = seen[-1][1]-i

        seen.append((T[i], i))

    return output

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])) # [0, 1, 4, 2, 1, 1, 0, 0]