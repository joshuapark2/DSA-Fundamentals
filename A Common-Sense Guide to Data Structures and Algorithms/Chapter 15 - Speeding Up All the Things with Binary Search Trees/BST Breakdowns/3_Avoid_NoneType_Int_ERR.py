'''
What's wrong with the code below?
Link: https://neetcode.io/problems/balanced-binary-tree?list=neetcode250

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def algo(node):
            if not node:
                return 0
            print(node.val)
            left = algo(node.left) + 1
            right = algo(node.right) + 1
            print(left, right, node.val)
        algo(root)
        if left != right:
            return False
        return True

Input: root=[1,2,3,null,null,4]
Output: 1
        2
        1 1 2

        
## The Fundamental Pattern is that you can't +1 when traversing
    - If a python function finishes without an explicit return statement, it implicitly returns None
    
    !! Because your algorithm doesn't have a return statement, it'll implicitly return None which will error
    - Also define variables first and use nonlocal inside our nested dfs function
'''
def isBalanced(root) -> bool:
    
    def algo(node):
        if not node:
            return 0
        print(node.val)
        left = algo(node.left) + 1
        right = algo(node.right) + 1
        print(left, right, node.val)

    algo(root)
    if left != right:
        return False
    return True
    