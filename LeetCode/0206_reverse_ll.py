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
def reverseList(head):
    p, bp = head, None
    while p:
        np = p.nxt
        p.nxt = bp
        bp = p
        p = np

    return bp

l = Node(1)
l.nxt = Node(2)
l.nxt.nxt = Node(3)
l.nxt.nxt.nxt = Node(4)
l.nxt.nxt.nxt.nxt = Node(5)

l = reverseList(l)
print(l)