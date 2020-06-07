from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def serialize(root):
    if not root: return ""

    data = [root.val]
    
    queue = deque([root])
    while queue:
        cur = queue.popleft()

        if cur.left:
            queue.append(cur.left)
            data.append(cur.left.val)
        else:
            data.append(None)

        if cur.right:
            queue.append(cur.right)
            data.append(cur.right.val)
        else:
            data.append(None)

    print(data)
    return ",".join(map(str, data))

def deserialize(data):
    if not data: return None

    data = [int(i) if i != "None" else None for i in data.split(",")]

    root = Node(data[0])
    i = 1

    queue = deque([root])
    while queue and i < len(data):
        cur = queue.popleft()
        
        if data[i] != None:
            cur.left = Node(data[i])
            queue.append(cur.left)
        i += 1
        
        if data[i] != None:
            cur.right = Node(data[i])
            queue.append(cur.right)
        i += 1

    return root

tree = "1,2,3,None,None,4,5"
print(serialize(deserialize(tree)))