class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def invertTree(root):
    if not root: return None

    root.left, root.right = root.right, root.left
    root.left = invertTree(root.left)
    root.right = invertTree(root.right)

    return root

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
root = invertTree(root)
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.left.left.val)
print(root.left.right.val)
print(root.right.left.val)
print(root.right.right.val)