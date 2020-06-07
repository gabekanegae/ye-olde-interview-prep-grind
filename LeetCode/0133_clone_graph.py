from collections import deque

class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors

def cloneGraph(root):
    if not root:
        return None

    new = {root: Node(root.val, [])}
    queue = deque([root])
    
    while queue:
        cur = queue.popleft()

        for neighbor in cur.neighbors:
            if neighbor not in new:
                new[neighbor] = Node(neighbor.val, [])
                queue.append(neighbor)

            new[cur].neighbors.append(new[neighbor])

    return new[root]