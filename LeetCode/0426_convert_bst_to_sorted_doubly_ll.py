class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

tail = None
head = None
def treeToDoublyList(root):
    def inOrder(root):
        global tail, head

        if not root: return

        l, r = root.left, root.right
        inOrder(l)
        if not head:
            root.right = root
            root.left = root
            head = root
            tail = root
        else:
            tail.right = root
            root.left = tail
            root.right = head
            head.left = root

            tail = tail.right
        inOrder(r)

    inOrder(root)
    return head

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

ll = treeToDoublyList(root)

p = ll
for _ in range(5):
    print(p.val, end=" ") # 1 2 3 4 5
    p = p.right

print("\n")

p = ll
for _ in range(5):
    print(p.val, end=" ") # 1 5 4 3 2
    p = p.left