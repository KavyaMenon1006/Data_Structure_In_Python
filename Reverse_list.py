def reverse(llist):
    prev = None
    cur = llist   
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev   
