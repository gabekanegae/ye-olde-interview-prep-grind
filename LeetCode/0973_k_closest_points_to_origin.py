from heapq import heappop, heappush

def distFromOrigin(p):
    return p[0]**2 + p[1]**2

def kClosest(points, K):
    heap = []
    for p in points:
        heappush(heap, (distFromOrigin(p), p))

    return [heappop(heap)[1] for _ in range(K)]

print(kClosest([[1, 3], [-2, 2]], 1)) # [[-2, 2]]

print(kClosest([[3, 3], [5, -1], [-2, 4]], 2)) # [[3,3], [-2,4]]