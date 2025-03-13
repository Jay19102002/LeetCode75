#           1           <---
#         /  \                  O
#        2    3        <---   /[ ]\
#       /                      /\
#      4               <---   person
#     / 
#    5                 <--- 
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
# Input: root = [1,2,3,4,null,null,null,5]
# Output: [1,3,4,5]

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rsv(root):
    if not root:
        return []
    
    que = []
    que.append(root)
    res = []
    res.append(root.val)

    while que:
        qlen = len(que)
        for i in range(qlen):
            node = que.pop(0)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        if que:
            res.append(que[-1].val)
    return res
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)

print(rsv(root))
