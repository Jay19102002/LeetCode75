# Input: head = [4,2,2,3]
# Output: 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def twinSum(head):
    max_sum = 0
    prev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    while slow:
        max_sum = max(max_sum, slow.val + prev.val)
        slow = slow.next
        prev = prev.next
    return max_sum

head = Node(4)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(3)

print(twinSum(head))