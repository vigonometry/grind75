from typing import Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getHeight(self, root):
        if not root:
            return -1
        if not (root.left or root.right):
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.left and root.right:
            return abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)
        if root.left:
            return self.getHeight(root.left) <= 0
        return self.getHeight(root.right) <= 0