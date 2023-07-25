# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not (root and p and q):
            return root
        if p.val < root.val and q.val < root.val: #search left if both are strictly less
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val: #search right if both are strictly greater
            return self.lowestCommonAncestor(root.right, p, q)
        return root