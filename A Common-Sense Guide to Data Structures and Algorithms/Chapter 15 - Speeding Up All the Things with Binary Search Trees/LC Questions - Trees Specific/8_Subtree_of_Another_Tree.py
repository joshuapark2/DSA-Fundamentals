'''
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        while root and root.val != subRoot.val:
            self.isSubtree(root.left, subRoot)
            self.isSubtree(root.right, subRoot)

        if root and subRoot and root.val == subRoot.val:
            return self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)
'''

def isSubtree(root, subRoot):
    if not root and not subRoot:
        return True
    
    while root and root.val != subRoot.val:
        isSubtree(root.left, subRoot)
        isSubtree(root.right, subRoot)
    
    if root and subRoot and root.val == subRoot.val:
        return isSubtree(root.left, subRoot.left) and isSubtree(root.right, subRoot.right)