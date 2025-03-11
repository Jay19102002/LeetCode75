#       1
#       \
#        1
#      / [\
#     1    1
#        /  \   
#       1    1
#       \]
#        1
#         \
#          1

# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longestpath(root):
    def dfs(root):
        if not root:
            return [-1,-1,-1]
        
        left = dfs(root.left)
        right = dfs(root.right)

        maxVal = max(left[1] + 1, right[0] + 1, left[2], right[2])

        return [left[1] + 1, right[0] + 1, maxVal]
    
    return dfs(root)[-1]

# Test the function
root = TreeNode(1)
root.right = TreeNode(1)
root.right.left = TreeNode(1)
root.right.right = TreeNode(1)    
root.right.right.left = TreeNode(1)
root.right.right.left = TreeNode(1)
root.right.right.right = TreeNode(1)
root.right.right.left.right = TreeNode(1)
root.right.right.left.right.right = TreeNode(1)

print(longestpath(root)) 