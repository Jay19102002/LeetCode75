#               10
#            /      \
#          [5       [-3
#       /    \        \
#      3]    2        11]
#    /  \     \
#   3   -2     1]
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(self, root, targetSum: int):
    def dfs(root,preSum):

        if not root:
            return 0
        
        currSum = preSum + root.val
        x = currSum - targetSum

        if x in freq:
            self.count += freq[x]
        
        if currSum in freq:
            freq[currSum] += 1
        else:
            freq[currSum] = 1

        dfs(root.left,currSum)
        dfs(root.right,currSum)
        freq[currSum] -=1

    self.count = 0
    freq = {0:1}
    dfs(root,0)
    return self.count

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)

targetSum = 8
print(pathSum(root,targetSum))