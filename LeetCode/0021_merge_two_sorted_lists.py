class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# O(n) time, O(1) space
def mergeTwoLists(l1, l2):
    if l1 and not l2: return l1
    if l2 and not l1: return l2
    if not l1 and not l2: return None

    p1, p2 = l1, l2
    if p1.val <= p2.val:
        l3 = p1
        p1 = p1.next
    else:
        l3 = p2
        p2 = p2.next

    p3 = l3

    while p1 and p2:
        if p1.val <= p2.val:
            p3.next = p1
            p1 = p1.next
        else:
            p3.next = p2
            p2 = p2.next
        p3 = p3.next

    if p1: p3.next = p1
    elif p2: p3.next = p2

    return l3

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(5)

l3 = mergeTwoLists(l1, l2)
p = l3
while p:
    print(p.val, end=" ")
    p = p.next
print()