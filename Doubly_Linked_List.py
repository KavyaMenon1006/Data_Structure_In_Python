class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
def reverse(head):
    if head is None:
        return None
    current = head
    new_head = None
    while current is not None:
        current.prev, current.next = current.next, current.prev
        new_head = current
        current = current.prev  # after swap, prev is the "next" node
    return new_head
