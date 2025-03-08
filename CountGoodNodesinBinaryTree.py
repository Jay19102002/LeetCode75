#                3
#              /  \
#             1   4
#            /   / \
#           3   1  5

# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root):
    def dfs(root,maxval):
        if not root:
            return 0
        
        if root.val >= maxval:
            count = 1
        else:
            count = 0
            
        maxval = max(maxval,root.val)
        count += dfs(root.left,maxval)
        count += dfs(root.right,maxval)
        return count
    return dfs(root,root.val)

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

print(countNodes(root))