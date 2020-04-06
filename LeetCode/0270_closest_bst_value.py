class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n) time, O(n) memory
def closestValue1(root, target):
    best = root.val
    
    stack = [root]
    while stack:
        cur = stack.pop()

        if abs(cur.val-target) < abs(best-target):
            best = cur.val

        if cur.left: stack.append(cur.left)
        if cur.right: stack.append(cur.right)

    return best

# O(h) time, O(1) memory
def closestValue2(root, target):
    best = root.val

    cur = root
    while cur:
        if abs(cur.val-target) < abs(best-target):
            best = cur.val
        
        if target < cur.val:
            cur = cur.left
        else:
            cur = cur.right

    return best

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(closestValue1(root, 3.714286)) # 4
print(closestValue2(root, 3.714286)) # 4