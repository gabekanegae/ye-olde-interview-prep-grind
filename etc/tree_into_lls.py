from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.left, self.right = None, None

    def __repr__(self): return str(self.data)

root = Node(1)
root.left = Node(2)
root.right = Node(4)

root.left.left = Node(3)
root.right.left = Node(7)
root.right.right = Node(8)

root.left.left.left = Node(9)
root.left.left.right = Node(11)
root.right.right.right = Node(14)
root.right.left.left = Node(16)
root.right.left.right = Node(4)

#           1
#      2        4
#   3   ?     7   8
# 9 11 ? ?  16 4 ? 14

levels = []
queue = deque([(root, 0)])

while queue:
    node, level = queue.popleft()

    if len(levels) < level+1:
        levels.append([])

    levels[level].append(node)

    for child in [node.left, node.right]:
        if not child: continue

        queue.append((child, level+1))

print(levels)

for level in levels:
    for i in range(len(level)):
        level[i].next = level[(i+1)%len(level)]

print(root.left.left.next)