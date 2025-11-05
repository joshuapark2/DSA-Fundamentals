'''
!! Reference: Trees_Specific/6_Balanaced_Binary_Tree.py !!


How does python implicitly know that we are updating left + 1 
    instead of right + 1 when going from 
    root 1 -> 2 -> subtree null null 
    and recursively going back up the call stack when calculating height?

Sample code from Trees_Specific/6_Balanaced_Binary_Tree.py
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


Concepts:
    - Function calls managed on the call stack
    - Local variable scoped
'''
# Calling height(node) creates its own execution frame on the call stack w/ own unique set of local variables (node, left, right)
# When the function finishes via `return`, its frame is removed from the stack and the returned value is sent back to the frame that originally called it.