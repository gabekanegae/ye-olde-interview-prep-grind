class Node:
    def __init__(self, data):
        self.data = data
        self.nxt = None

    def __str__(self):
        s = []
        p = self
        while p:
            s += str(p.data)
            p = p.nxt
        return "[" + ", ".join(s) + "]"

# O(n) time, O(1) space
def middleNode(head):
    i, j = head, head
    while j and j.nxt:
        i = i.nxt
        j = j.nxt.nxt
    return i

l = Node(1)
l.nxt = Node(2)
l.nxt.nxt = Node(3)
l.nxt.nxt.nxt = Node(4)
l.nxt.nxt.nxt.nxt = Node(5)
l.nxt.nxt.nxt.nxt.nxt = Node(6)
l.nxt.nxt.nxt.nxt.nxt.nxt = Node(7)
l.nxt.nxt.nxt.nxt.nxt.nxt.nxt = Node(8)

print(middleNode(l).data)