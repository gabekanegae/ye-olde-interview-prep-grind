class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# O(n) time, O(n) memory
def hasCycle(head):
    seen = set()

    p = head
    while p:
        if (p.val, p.next) in seen: return True
        seen.add((p.val, p.next))
        p = p.next
    return False

# O(n) time, O(1) memory
def hasCycle2(head):
    i, j = head, head

    while i and j:
        try:
            i = i.next
            j = j.next.next
        except AttributeError:
            return False

        if i is j: return True

    return False

l = ListNode(3)
l.next = ListNode(2)
l.next.next = ListNode(0)
l.next.next.next = ListNode(-4)
l.next.next.next.next = l.next
print(hasCycle(l))
print(hasCycle2(l))

l = ListNode(3)
l.next = ListNode(2)
l.next.next = l
print(hasCycle(l))
print(hasCycle2(l))