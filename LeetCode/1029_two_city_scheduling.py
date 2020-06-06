def twoCitySchedCost(costs):
    costs.sort(key=lambda x: x[0]-x[1])

    mid = len(costs)//2
    return sum(c[0] for c in costs[:mid]) + sum(c[1] for c in costs[mid:])

print(twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]])) # 110