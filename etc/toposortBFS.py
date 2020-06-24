from collections import deque

def toposort(depends):
    dependsAmt = {k: len(v) for k, v in depends.items()}

    unlocks = {k: [] for k in depends}
    for k, v in depends.items():
        for d in v: unlocks[d].append(k)

    order = []
    queue = deque([k for k in depends if dependsAmt[k] == 0])
    while queue:
        cur = queue.popleft()
        order.append(cur)
        for d in unlocks[cur]:
            dependsAmt[d] -= 1
            if dependsAmt[d] == 0:
                queue.append(d)

    if len(order) == len(depends):
        return "".join(order)
    else:
        return -1

depends = {
           "a": "bcd",
           "b": "ed",
           "c": "eb",
           "d": "",
           "e": "d",
           "f": "a"
          }

print(toposort(depends))

depends = {
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

print(toposort(depends))
depends["d"] += "a"
print(toposort(depends)) # CYCLE