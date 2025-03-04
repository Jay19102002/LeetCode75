# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

# reverse Linked list
def reversell(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
printList(head)

head = reversell(head)
printList(head)  