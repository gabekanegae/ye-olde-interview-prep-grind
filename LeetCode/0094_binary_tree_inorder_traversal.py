class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversalRecursive(root):
    arr = []
    def rec(root):
        if not root: return

        if root.left: rec(root.left)
        arr.append(root.val)
        if root.right: rec(root.right)

    rec(root)
    return arr

def inorderTraversalIterative(root):
    arr = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        arr.append(cur.val)
        cur = cur.right

    return arr

#   2
# 1   3

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(inorderTraversalRecursive(root)) # [1, 2, 3]
print(inorderTraversalIterative(root)) # [1, 2, 3]

#       5
#    1      4
# x    x  3   6

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(inorderTraversalRecursive(root)) # [None, 1, None, 5, 3, 4, 6]
print(inorderTraversalIterative(root)) # [1, 2, 3]

#         10
#     5       15
# x      x  6     20

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)
print(inorderTraversalRecursive(root)) # [None, 5, None, 10, 6, 15, 20]
print(inorderTraversalIterative(root)) # [1, 2, 3]