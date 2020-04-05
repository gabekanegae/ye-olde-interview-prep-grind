class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isValidBST(root):
    arr = []
    def inOrderTraversal(root):
        if not root: return

        if root.left: inOrderTraversal(root.left)
        arr.append(root.val)
        if root.right: inOrderTraversal(root.right)

    inOrderTraversal(root)

    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return False
    return True

#   2
# 1   3

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(isValidBST(root)) # True

#       5
#    1      4
# x    x  3   6

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(isValidBST(root)) # False

#         10
#     5       15
# x      x  6     20

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)
print(isValidBST(root)) # False