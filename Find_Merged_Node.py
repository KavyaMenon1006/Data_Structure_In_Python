def findMergeNode(head1, head2):
    pointer1, pointer2 = head1, head2
    while pointer1 != pointer2:
        pointer1 = pointer1.next if pointer1 else head2
        pointer2 = pointer2.next if pointer2 else head1
