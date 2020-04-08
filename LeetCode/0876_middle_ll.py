class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        s = []
        p = self
        while p:
            s += str(p.data)
            p = p.next
        return "[" + ", ".join(s) + "]"

# O(n) time, O(1) space
def middleNode(head):
    i, j = head, head
    while j and j.next:
        i = i.next
        j = j.next.next
    return i

l = Node(1)
l.next = Node(2)
l.next.next = Node(3)
l.next.next.next = Node(4)
l.next.next.next.next = Node(5)
l.next.next.next.next.next = Node(6)
l.next.next.next.next.next.next = Node(7)
l.next.next.next.next.next.next.next = Node(8)

print(middleNode(l).data)