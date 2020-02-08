class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# O(s) time, O(1) space, two-pass
def removeNthFromEnd(head, n):
    i, j = head, head

    # "Given n will always be valid."
    for _ in range(n):
        j = j.next

    # n == len(head) aka remove first element
    if j == None: return i.next

    while j:
        j = j.next
        if j:
            i = i.next

    i.next = i.next.next
    return head

##########
# Helper functions, not related to the problem itself

def buildLL(l):
    ll = ListNode(None)
    p = ll
    for e in l:
        p.next = ListNode(e)
        p = p.next
    return ll.next

def printLL(ll):
    p = ll
    while p:
        print(p.val, end=" ")
        p = p.next
    print()

##########

l = removeNthFromEnd(buildLL([1, 2, 3, 4, 5, 6]), 2)
printLL(l)