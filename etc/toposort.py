# O(V+E) time, O(V) space, NO CYCLE DETECTION
def topoSort(g):
    reverseOrder = []
    done = set()

    def rec(node):
        if node in done: return
        done.add(node)

        for a in g[node]: rec(a)
        reverseOrder.append(node)

    for a in g: rec(a)
    return "".join(reverseOrder[::-1])

# O(V+E) time, O(V) space
def topoSortCycle(g):
    reverseOrder = []
    doing = set()
    done = set()

    def rec(node):
        if node in doing:
            return -1

        if node in done: return
        doing.add(node)

        for a in g[node]:
            if rec(a) == -1: return -1

        reverseOrder.append(node)
        doing.remove(node)
        done.add(node)

    for a in g:
        if rec(a) == -1: return "CYCLE"

    return "".join(reverseOrder[::-1])

g = {
     "a": "d",
     "b": "d",
     "c": "ab",
     "d": "hg",
     "e": "adf",
     "f": "kj",
     "g": "i",
     "h": "ij",
     "i": "l",
     "j": "lm",
     "k": "j",
     "l": "",
     "m": ""
    }

print(topoSort(g)) # efkcbadghjmil
g["d"] += "a"
print(topoSortCycle(g)) # CYCLE