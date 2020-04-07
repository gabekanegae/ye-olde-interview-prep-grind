class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    result = ListNode(-1)
    l3 = result
    carry = 0

    while l1 and l2:
        s = l1.val + l2.val
        
        if carry:
            s += 1
            carry = 0

        l3.next = ListNode(s % 10)
        carry = s // 10

        l1 = l1.next
        l2 = l2.next
        l3 = l3.next

    l = l1 or l2
    while l:
        s = l.val

        if carry:
            s += 1
            carry = 0

        l3.next = ListNode(s % 10)
        carry = s // 10

        l = l.next
        l3 = l3.next

    if carry:
        l3.next = ListNode(1)

    return result.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

l3 = addTwoNumbers(l1, l2)
while l3:
    print(l3.val, end=" ") # 7 0 8
    l3 = l3.next

print()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(0)

l3 = addTwoNumbers(l1, l2)
while l3:
    print(l3.val, end=" ") # 2 4 3
    l3 = l3.next