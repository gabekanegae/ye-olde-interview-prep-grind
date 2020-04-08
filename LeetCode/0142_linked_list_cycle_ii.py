def detectCycle(head):
    turtle = head
    hare = head
    
    while turtle and hare and hare.next:
        turtle = turtle.next
        hare = hare.next.next
        
        if turtle is hare:
            break
    
    if not turtle or not hare or not hare.next:
        return None
    
    start = head
    while start and turtle:
        if start is turtle:
            return start
        
        start = start.next
        turtle = turtle.next