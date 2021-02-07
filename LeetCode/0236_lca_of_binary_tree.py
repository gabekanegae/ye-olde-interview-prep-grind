class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    if not root: return None
    if root is p or root is q: return root

    inLeft = lowestCommonAncestor(root.left, p, q)
    inRight = lowestCommonAncestor(root.right, p, q)

    if inLeft and inRight: return root
    return inLeft or inRight

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

print(lowestCommonAncestor(root, root.left, root.right).val) # 3

print(lowestCommonAncestor(root, root.left, root.left.right).val) # 5

root = TreeNode(1)
root.left = TreeNode(2)

print(lowestCommonAncestor(root, root, root.left).val) # 1

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

print(lowestCommonAncestor(root, root.left, root.left.right.right).val) # 5