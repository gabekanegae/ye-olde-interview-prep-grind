from heapq import heappush, heappop

def lastStoneWeight(stones):
    heap = []
    for stone in stones:
        heappush(heap, -stone)

    while len(heap) > 1:
        new = abs(heappop(heap) - heappop(heap))
        heappush(heap, -new)

    return -heappop(heap)

print(lastStoneWeight([2, 7, 4, 1, 8, 1])) # 1