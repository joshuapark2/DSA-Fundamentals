'''
Why can't we just use the code below?

    left = algo(node.left) + 1
    right = algo(node.right) + 1

How exactly does 1 + max(left, right) work?

Note: Referencing 6_Balanaced_Binary_Tree.py
 - Recursion/1_Understanding_Call_Stack.py for more details
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
        
        return max(left, right) + 1
    
    height(root)
    return balanacedTree
'''
Input: root = [1,2,3,null,null,4,null,5]

      1                      1 = [1, 2]
     / \
    2   3                    2 = [null, null, 4, null]
       /
      4                      3 = [5, null]
     /
    5                        4 = [null, null] - (implicit null)

How the Call Stack works:
    - Calling height(node) creates its own execution frame on the call stack w/ own unique set of local variables (node, left, right)
    - When the function finishes via `return`, its frame is removed from the stack and the returned value is sent back to the frame that originally called it.

    Tracing [Nodes: 1 (root), 2 (left of 1), 3 (right of 1), 4 (right of 2), 5 (right of 4)]

        height(node=1) frame is created
            calling height(node.left) for node=2
            pausing node=1 frame waiting for a result

        height(node=2) frame is created
            calling height(node.left) for node=None)
            pausing node=2 frame waiting for a result
        
        height(node=None) frame is created
            if not node: returns 0 immediately 
            destory frame and value 0 is returned to node=2 frame
        
        height(node=2) with returned value 0 stored in local variable left since we called left = height(node.left)

    Pattern:
        1. Resolve the call height(node.left) completely.
        2. Store the result in the current frame's local left variable.
        3. Resolve the call height(node.right) completely.
        4. Store the result in the current frame's local right variable.
'''

# Going back to max(left, right) + 1 and our example
'''
Input: root = [1,2,3,null,null,4,null,5]

      1                      1 = [1, 2]
     / \
    2   3                    2 = [null, null, 4, null]
       /
      4                      3 = [5, null]
     /
    5                        4 = [null, null] - (implicit null)

dfs(node=1)
    left = dfs(node.left)
        dfs(node=2)
            left = dfs(node.left)
                dfs(node=None)
                    if not node: return 0
---------------------------------------------------------------
            left = dfs(node.left = 0) -> left = dfs(0) 
                -> left = 0

            right = dfs(node.right)
                dfs(node=None)
                    if not node: return 0
            
            right = dfs(node.right = 0) -> right = dfs(0) 
                -> right = 0
---------------------------------------------------------------
            return max(left, right) + 1 -> max(left = 0, right = 0) + 1 -> max(0) + 1
        
        dfs(node=2 -> returned value 1)
    left = dfs(node.left = 1) -> left = dfs(1)
        -> left = 1

    Repeat process with right = dfs(node.right)
'''