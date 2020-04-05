class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def minDepth(root):
    if not root: return 0

    if root.left and root.right:
        return 1 + min(minDepth(root.left), minDepth(root.right))

    if root.left: return 1 + minDepth(root.left)
    if root.right: return 1 + minDepth(root.right)

    return 1

#   2
# 1   3

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(minDepth(root)) # 2

#       5
#    1      4
# x    x  3   6

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(minDepth(root)) # 2

#            10
#       5         15
#   2      x    6      20
# x   x  x  x  x  x  4    x

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)
root.right.right.left = TreeNode(4)
print(minDepth(root)) # 3