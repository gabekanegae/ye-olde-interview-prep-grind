from heapq import heappush, heappop

class Graph:
    def __init__(self, amt):
        self.vertices = [chr(ord("a")+c) for c in range(amt)]
        self.edges = {k: set() for k in self.vertices}

    def addUndirectedEdge(self, a, b, w):
        self.addDirectedEdge(a, b, w)
        self.addDirectedEdge(b, a, w)

    def addDirectedEdge(self, a, b, w):
        self.edges[a].add((b, w))

    # Dijkstra
    def simplestLongestTimeToReachAll(self, start):
        dist = {k: 9999 for k in self.vertices}
        dist[start] = 0

        for a in self.vertices:
            for b, w in self.edges[a]:
                dist[b] = min(dist[b], dist[a] + w)

        return max(dist.values())

    # Dijkstra with predecessor list to build the tree
    def longestTimeToReachAll(self, start):
        dist = {k: 9999 for k in self.vertices}
        dist[start] = 0

        pred = {k: None for k in self.vertices}

        for a in self.vertices:
            for b, w in self.edges[a]:
                if dist[a] + w < dist[b]:
                    dist[b] = dist[a] + w
                    pred[b] = a

        # print(dist)
        # print(pred)
        return max(dist.values())

    # Dijkstra with priority queue for optimal O(E log V), assuming a fib-heap
    def betterLongestTimeToReachAll(self, start):
        dist = {k: float("inf") for k in self.vertices}
        dist[start] = 0

        pred = {k: None for k in self.vertices}

        done = set([start])
        heap = [(0, start)]
        while heap:
            # print(heap)
            a = heappop(heap)[1]

            for b, w in self.edges[a]:
                if b not in done:
                    if dist[a] + w < dist[b]: # if b in done, this will always be false (assuming all weights > 0)
                        dist[b] = dist[a] + w
                        pred[b] = a
                    heappush(heap, (dist[b], b))

            done.add(a)

        print(dist)
        print(pred)
        return max(dist.values())

# https://www.youtube.com/watch?v=eFZCPlZCyIM
g = Graph(8)
g.addUndirectedEdge("a", "b", 3)
g.addUndirectedEdge("a", "c", 4)
g.addUndirectedEdge("a", "d", 7)
g.addUndirectedEdge("b", "c", 1)
g.addUndirectedEdge("b", "f", 5)
g.addUndirectedEdge("c", "d", 2)
g.addUndirectedEdge("c", "f", 6)
g.addUndirectedEdge("d", "e", 3)
g.addUndirectedEdge("e", "f", 1)
g.addUndirectedEdge("d", "g", 6)
g.addUndirectedEdge("e", "g", 3)
g.addUndirectedEdge("e", "h", 4)
g.addUndirectedEdge("f", "h", 8)
g.addUndirectedEdge("g", "h", 2)

print(g.simplestLongestTimeToReachAll("a"))
print(g.longestTimeToReachAll("a"))
print(g.betterLongestTimeToReachAll("a"))

print()

# https://www.youtube.com/watch?v=K_1urzWrzLs
g = Graph(7)
g.addUndirectedEdge("a", "b", 2)
g.addUndirectedEdge("a", "c", 4)
g.addUndirectedEdge("a", "d", 7)
g.addUndirectedEdge("a", "f", 5)
g.addUndirectedEdge("b", "d", 6)
g.addUndirectedEdge("b", "e", 3)
g.addUndirectedEdge("b", "g", 8)
g.addUndirectedEdge("c", "f", 6)
g.addUndirectedEdge("d", "f", 1)
g.addUndirectedEdge("d", "g", 6)
g.addUndirectedEdge("f", "g", 6)
g.addUndirectedEdge("e", "g", 7)

print(g.simplestLongestTimeToReachAll("a"))
print(g.longestTimeToReachAll("a"))
print(g.betterLongestTimeToReachAll("a"))



'''
costs = [9999 for n in nodes]
costs[start] = 0

for a in nodes:
    for b, w in a.edges:
        costs[b] = min(costs[a]+w, costs[b])

-- OR --

costs = [9999 for n in nodes]
costs[start] = 0

heap = [(0, start)]
seen = set()
while heap:
    _, a = heappop(heap)
    seen.add(a)

    for b, w in a.edges:
        if b in seen: continue
        
        costs[b] = min(costs[a]+w, costs[b])
        heappush(heap, (costs[b], b))
'''