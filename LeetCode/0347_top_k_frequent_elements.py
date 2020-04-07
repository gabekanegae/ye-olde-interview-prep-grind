from heapq import heappush, heappop

def topKFrequent(nums, k):
    count = dict()
    for n in nums:
        if n not in count: count[n] = 0
        count[n] += 1

    heap = []
    for n, ct in count.items():
        heappush(heap, (-ct, n))

    return [heappop(heap)[1] for _ in range(k)]

print(topKFrequent([1, 1, 1, 2, 2, 3], 2)) # [1, 2]
print(topKFrequent([1], 1)) # [1]