#           4
#         /  \
#        2    7
#       / \
#      1   3

# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    elif val < root.val:
        return searchBST(root.left, val)
    elif val > root.val:
        return searchBST(root.right, val)
    
        
    
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

val = 2
print(searchBST(root, val))  