def insertNodeAtTail(head, data):

    new_node = SinglyLinkedListNode(data)
    if head is None:
        return new_node
    
    tail = head
    while tail.next:
        tail = tail.next
    tail.next = new_node
    return head
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head
