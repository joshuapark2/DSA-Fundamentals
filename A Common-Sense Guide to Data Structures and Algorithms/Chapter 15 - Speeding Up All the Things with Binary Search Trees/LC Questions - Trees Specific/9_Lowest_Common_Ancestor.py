'''
https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree?list=neetcode250

LC Solution
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

Solution:
    - I got stuck on how the two descendants would recognize the ancestor, but
        if you flip the question on its head, you realize that we can move our root
        node instead of p or q.
    - Comparison of p and q, using root, max(), min()
    - This works because of the fundamental nature of how root will always have
        a value equal or less than and equal or greater than the ancestor.
        - max() being greater than means we need to increase our value going right to
            higher numbers than root
        - min() being less than means we need to decrease our value by going left
            to lower numbers than roto.
        - Iterate is done via moving root and returning that last to get our answer.

'''

def lowestCommonAncestor(root, p, q):
    if not root or not p or not q:
        return None
    
    if (max(p.val, q.val) < root.val):
        return lowestCommonAncestor(root.left, q, p)
    elif (min(p.val, q.val) > root.val):
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root