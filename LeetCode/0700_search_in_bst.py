class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def searchBST(root, val):
    cur = root
    while cur:
        if cur.val == val:
            return cur

        if cur.val > val:
            cur = cur.left
        elif cur.val < val:
            cur = cur.right

    return None

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(searchBST(root, 2).val) # 2
print(searchBST(root, 3).val) # 3

print(searchBST(None, 7)) # None