# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node. 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(7)
head.next.next.next.next = Node(1)
head.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next = Node(6)

#delete at node
def deleteAtPosition(head):
    if head is None:
        return head
    
    fast = head
    slow = head
    prev = None

    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    
    prev.next = slow.next
    return head

while head:
    print(head.data, end = " ")
    head = head.next

