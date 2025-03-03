# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

def oddEven(head):
    if not head or not head.next:
        return head
    odd = head
    even = head.next
    evenHead = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
        odd.next = evenHead
    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

printList(head)

head = oddEven(head)
printList(head)