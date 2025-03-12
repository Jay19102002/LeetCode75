
#               3
#             /   \
#            5     1
#          / \    / \
#        6   2   0  8
#           / \
#          7   4

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Explanation: The LCA of nodes 5 and 1 is 3.
# Output: 3

# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca(root,p,q):
    def dfs(root):
        if not root:
            return False
        
        if root.val == p or root.val == q:
            return root.val
        
        left = dfs(root.left)
        right = dfs(root.right)

        if left and right:
            return root.val
            
        return left if left else right
    
    return dfs(root) if dfs(root) else -1
        
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

p = 5
q = 1

print(lca(root,p,q))