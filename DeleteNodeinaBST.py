#           5
#          / \
#         3   6
#        / \   \
#       2   4   7

# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def findMin(root):
    while root.left:
        root = root.left
    return root

def deleteNode(root, key):
    if not root:
        return None
    elif key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left and not root.right:
            root = None
            
        elif not root.left:
            root = root.right
        elif not root.right:
            root = root.left
        else:
            # Find the node with the minimum value in the right subtree
            temp = findMin(root.right)
            root.val = temp.val
            root.right = deleteNode(root.right, temp.val)
    return root

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

print(deleteNode(root, 3).val)  