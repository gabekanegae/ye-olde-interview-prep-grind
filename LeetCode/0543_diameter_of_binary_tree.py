class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def diameterOfBinaryTree(root):
    diameter = 0

    def depth(root):
        nonlocal diameter

        if not root: return 0

        ld, rd = depth(root.left), depth(root.right)
        diameter = max(diameter, ld + rd)

        return 1 + max(ld, rd)

    depth(root)
    return diameter

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(diameterOfBinaryTree(root))