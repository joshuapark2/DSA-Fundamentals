# Link: https://neetcode.io/problems/balanced-binary-tree?list=neetcode250

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
1. Understand the problem w/ examples
2. Naive Solution - Recursive DFS O(n) where n is each node visited.
3. Efficient Solution -> Solve bottom-up instead of top-down by checking if the base case is balanced and working up.
    Each node is visited once
    - We don't need to visit every node since we are getting the height of the subtree for each subtree, taking the difference <= 1 at root node
      to determine if it's balanaced.
    - As we work our way up, we determine the entire height by taking the max of left and right subtree + root tree recursively.
    - Again taking the * difference * is how check if it's balanced.

returning [T/F boolean, height of subtree] for this algorithm.
    - If any subtree is not balanced, we return false.
'''
# More readable version
'''
1. variable answer

2. base case
3. dfs traversal
4. conditional
5. recursion

6. call + answer
'''
def isBalanced(root):
    balanacedTree = True

    def height(node):
        nonlocal balanacedTree

        if not node:
            return 0
        
        left = height(node.left)
        right = height(node.right)

        if abs(left - right) > 1:
            balanacedTree = False
            return 0
        
        return 1 + max(left, right)
    
    height(root)
    return balanacedTree


# NeetCode Solution Below
# Why can't we just use the outer function - we need to return two values
def isBalanced_NeetCode(root):
    def dfs(node):
        if not node:
            return [True, 0] # Boolean of balanced and default 0 height

        # Calling dfs recursively and assign to result variables.
        left, right = dfs(node.left), dfs(node.right)
        # From the root node is it balanced? -> Need two conditionals
        # 1. Is the left and right subtree balanced? -> left[0] and right[0]
        # 2. Is the root itself also balanaced -> abs(left[1] - right[1]) <= 1
        balanced = (left[0] and right[0] and 
                    abs(left[1] - right[1]) <= 1)
        return [balanced, 1 + max(left[1], right[1])] 
        # balanced -> gives balanced from root and entire tree balanced at all -> This only true if l and r are balanced and root is balanaced from two conditionals
        # 1 + max(left[1], right[1] -> Giving us height) 
    
    return dfs(root)[0] # Syntax to return the boolean value.


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def algo(node):
            if not node:
                return [True, 0]
            
            left, right = algo(node.left), algo(node.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        
        return algo(root)[0]
