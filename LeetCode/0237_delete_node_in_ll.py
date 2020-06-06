class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)

deleteNode(root.next.next)

p = root
while p:
    print(p.val, end=" ")
    p = p.next
print()