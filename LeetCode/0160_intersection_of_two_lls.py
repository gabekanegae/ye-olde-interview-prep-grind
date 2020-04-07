class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getSize(head):
    count = 0
    while head:
        count += 1
        head = head.next

    return count

def getIntersectionNode(headA, headB):
    sizeA = getSize(headA)
    sizeB = getSize(headB)

    if sizeA > sizeB:
        sizeA, sizeB = sizeB, sizeA
        headA, headB = headB, headA

    for _ in range(sizeB-sizeA):
        headB = headB.next

    while headA and headB:
        if headA is headB: return headA

        headA = headA.next
        headB = headB.next

    return None

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

l2 = ListNode(10)
l2.next = ListNode(20)
l2.next.next = l1.next.next

print(getIntersectionNode(l1, l2).val) # 3

l2 = ListNode(10)
l2.next = ListNode(20)

print(getIntersectionNode(l1, l2)) # None