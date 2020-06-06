from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isCousins(root, x, y):
    queue = deque([root])

    while queue:
        isCousin = False
        isSibling = False

        width = len(queue)
        for _ in range(width):
            cur = queue.popleft()

            if not cur:
                isSibling = False
                continue

            if cur.val in [x, y]:
                if not isCousin:
                    isCousin = True
                    isSibling = True
                else:
                    return not isSibling

            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)

            queue.append(None)

    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.right = Node(5)

print(isCousins(root, 5, 4)) # True