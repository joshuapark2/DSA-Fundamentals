'''
Link: https://neetcode.io/problems/same-binary-tree?list=neetcode250

1. Base Case
2. Conditionals for T/F
'''
def isSameTree(self, p, q):
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False

'''
My attempt:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        answer = True

        def comparison(p, q):
            nonlocal answer

            if not p or not q:
                return None
            
            comparison(p.left, q.left)
            comparison(p.right, q.right)
            print(p.val, q.val)
            if p == q:
                return answer
            else:
                answer = False
                return answer
        
        comparison(p, q)
        return answer
'''