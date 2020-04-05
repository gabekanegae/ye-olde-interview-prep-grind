from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrder(root):
    levels = []

    if not root: return []

    queue = deque([(root, 0)])
    while queue:
        cur, curLevel = queue.popleft()

        if curLevel == len(levels):
            levels.append([])

        levels[curLevel].append(cur.val)

        if cur.left: queue.append((cur.left, curLevel+1))
        if cur.right: queue.append((cur.right, curLevel+1))

    return levels

#   2
# 1   3

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(levelOrder(root)) # [[2], [1, 3]]

#       5
#    1      4
# x    x  3   6

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(levelOrder(root)) # [[5], [1, 4], [3, 6]]

#         10
#     5       15
# x      x  6     20

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)
print(levelOrder(root)) # [[10], [5, 15], [6, 20]]