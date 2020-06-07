from collections import deque

class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors

def cloneGraph(root):
    if not root:
        return None

    new = {root.val: Node(root.val, [])}
    queue = deque([root])
    
    while queue:
        cur = queue.popleft()

        for neighbor in cur.neighbors:
            if neighbor.val not in new:
                new[neighbor.val] = Node(neighbor.val, [])
                queue.append(neighbor)

            new[cur.val].neighbors.append(new[neighbor.val])

    return new[root.val]