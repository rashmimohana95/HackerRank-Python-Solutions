

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    d = []
    while head1 or head2:
        if head1:
            d.append(head1.data)
            head1 = head1.next
        if head2:
            d.append(head2.data)
            head2 = head2.next
    d.sort()
    output = SinglyLinkedList()
    for i in range(len(d)):
        output.insert_node(d[i])
    return output.head
    
