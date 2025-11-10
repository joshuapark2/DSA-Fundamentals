'''
Referring to 7_Is_Same_Tree.py

if p and q and p.val == q.val:
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

p and q makes sure both nodes are valid and not null
p.val == q.val executed if p and q is successful and checks that both existing nodes
    has the same value

!! This is important to avoid NoneType Errors !!
'''