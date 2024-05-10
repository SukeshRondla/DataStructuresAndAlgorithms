class Solution:
    # Definition for a binary tree node.
     class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is None or one of the nodes is found, return root
        if root is None or root == p or root == q:
            return root
 
        # Recursively search left and right subtrees for the LCA
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right subtrees return non-None, it means p and q are found in different subtrees, s.  o root is the LCA
        if left and right:
            return root
        
        # If either left or right subtree returns non-None, return that (the common ancestor)
        return left or right
