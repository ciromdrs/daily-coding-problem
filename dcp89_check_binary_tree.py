'''Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and
satisfies the constraint that the key in the left child must be less
than or equal to the root and the key in the right child must be
greater than or equal to the root.'''

class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left  = left
        self.right = right

def check(n):
    if n == None:
        return True
    
    res = True
    if n.left != None:
        res = res and (n.left.value <= n.value)
    if n.right != None:
        res = res and (n.right.value >= n.value)
    return res and check(n.left) and check(n.right)

A = Node(5,
         Node(3,
              Node(1),
              Node(3)
             ),
         Node(7,
              Node(7)
         )
    )

B = Node(6, A, Node(5))

print(check(A))
print(check(B))
