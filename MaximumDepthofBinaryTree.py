#           3
#          / \
#         9   20
#            / \
#           15  7
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def depthBT(self, root):
    if root is None:
        return 0
    # return 1 + max(self.depthBT(root.left), self.depthBT(root.right))
    else:
        left_depth = self.depthBT(root.left)
        right_depth = self.depthBT(root.right)
    return max(left_depth, right_depth) + 1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(depthBT(root))