from heapq import heappush, heappop

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, other):
        return self.val < other.val

def mergeKLists(lists):
    result = ListNode(-1)
    p = result

    heap = []
    for l in lists:
        if l: heappush(heap, l)

    while heap:
        cur = heappop(heap)
        if cur.next: heappush(heap, cur.next)
        p.next = cur
        p = p.next

    return result.next

l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

l3 = mergeKLists([l1, l2, l3])
p = l3
while p:
    print(p.val, end=" ") # 1 1 2 3 4 4 5 6
    p = p.next

print()