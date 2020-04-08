def oddEvenList(head):
    if not head: return None

    even = ListNode(None)
    o, e = head, even
    
    while o.next:
        e.next = o.next
        e = e.next
        
        if o.next.next:
            o.next = o.next.next
            o = o.next
        else:
            break
        
        e.next = None
    
    o.next = even.next
    
    return head