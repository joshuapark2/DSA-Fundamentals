# Link: https://leetcode.com/problems/delete-node-in-a-bst/description/
'''
NeetCode Solution
'''
def deleteNode(self, root, key):
    if not root:
        return root

    # 1. Searching for correct node to delete
    if root.val > key:
        root.left = self.deleteNode(root.left, key)
    elif root.val < key:
        root.right = self.deleteNode(root.right, key)

    # 2. Deleting the node
    else:
        # Case 1: 0 or 1 node + deleting process
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Searching for successor or the next largest value -> Swap -> Replace with None
        curr = root.right
        while curr.left:
            curr = curr.left
        root.val = curr.val
        root.right = self.deleteNode(root.right, root.val)

    return root



'''
Personal Solution
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1. 5 > 3 -> left node equals recursive left (we are going left)
2. We reached our target node 3 that we have to delete -> go to else statement:
    - We have two children and call our getSuccessor helper function
        - node 3 = node 4
        - go left from node 4 -> nothing is left, so we return node 4
    - Now node 3 equals node 4 in-place value swap
    - delete via: node right 4 = deleteNode(node 4, 4)
        - Reach our node with 0 or 1 children case and end up returning node None
    - node None is now replacing root.right
'''

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # Getting the next available largest value
        '''
        The logic is that curr.right gives us the next largest value since we
            confirmed a node with 2 children
        From here we find the next largest by going left to find any values 
            in-between our root and next largest ex. node 3 -> 5 -> 4

        '''
        def getSuccessor(curr):
            curr = curr.right
            while curr is not None and curr.left is not None:
                curr = curr.left
            return curr

        if root is None:
            return root

        # 1. Searching for our target node to delete
        # If our value is too high, we need to go left to find a lower value
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        # If our value is too low, we need to go right to find higher value
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        # Otherwise, we've reached our target and need to remove based on 3 cases
        else:
            '''
            Case 1: Node w/ 0 or 1 children eventually leads to 
                    a node with 0 children, giving us root.left or root.right
                    returning none to insert into root.right at the very
            '''
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            # Case 2: Node with 2 children:
            # Get next largest -> Swap with next largest value
            successor = getSuccessor(root)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        
        return root
