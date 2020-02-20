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

# O(n) time, O(1) space
def middleNode(head):
    i, j = head, head
    while j and j.nxt:
        i = i.nxt
        j = j.nxt.nxt
    return i

# O(n) time, O(1) space
def isPalindrome(head):
    half1 = head
    half2 = middleNode(head)


    half2 = reverseList(half2)

    p1, p2 = half1, half2
    while p1 and p2:
        if p1.data != p2.data:
            return False
        p1 = p1.nxt
        p2 = p2.nxt

    # Restore original list
    half2 = reverseList(half2)

    return True

l = Node(1)
l.nxt = Node(2)
l.nxt.nxt = Node(1)

# print(l)
print(isPalindrome(l))
# print(l)