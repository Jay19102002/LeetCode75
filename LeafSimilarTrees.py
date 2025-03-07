#            3                      3
#          /  \                   /   \
#         5    1                5      1
#       / \   / \             /  \   /  \
#      6  2  9  8            6   7  4   2
#        / \                           / \
#       7  4                          9  8
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def similarTrees(root1,root2):
    def dfs(root,leaf):
        if not root:
            return 
        
        if not root.left and not root.right:
            leaf.append(root.val)
            return
        
        dfs(root.left,leaf)
        dfs(root.right,leaf)

    leaf1, leaf2 = [],[]
    dfs(root1,leaf1)
    dfs(root2,leaf2)
    return leaf1 == leaf2
    
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)

root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)

print(similarTrees(root1,root2))