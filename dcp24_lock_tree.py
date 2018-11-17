'''Implement locking in a binary tree. A binary tree node can be locked
or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

    is_locked, which returns whether the node is locked
    lock, which attempts to lock the node. If it cannot be locked, then
        it should return false. Otherwise, it should lock it and return
        true.
    unlock, which unlocks the node. If it cannot be unlocked, then it
        should return false. Otherwise, it should unlock it and return
        true.
        
You may augment the node to add parent pointers or any other property
you would like. You may assume the class is used in a single-threaded
program, so there is no need for actual locks or mutexes. Each method
should run in O(h), where h is the height of the tree.'''

class Node:
    def __init__(self, value, left=None, right=None):
        self.value  = value
        self.parent = None
        self.locked = False
        self.left   = left
        self.right  = right
        if left:
            self.left.parent  = self
        if right:
            self.right.parent = self
        
    def is_locked(self):
        return self.locked or self.parent_children_locked()

    def parent_children_locked(self):
        return self._parent_locked() or self._children_locked()

    def _parent_locked(self):
        if self.parent == None:
            return False
        return self.parent.locked or self.parent._parent_locked()
        
    def _children_locked(self):
        left_locked  = False
        right_locked = False
        if self.left:
            left_locked  = self.left.locked  or self.left._children_locked()
        if self.right:
            right_locked = self.right.locked or self.right._children_locked()
        return left_locked or right_locked
        
    def lock(self):
        if not self.parent_children_locked() and not self.locked:
            self.locked = True
            return True
        return False
        
    def unlock(self):
        if not self.parent_children_locked() and self.locked:
            self.locked = False
            return True
        return False

'''
    root
   /    \
   l    r
  / \  /
 ll lr rl
'''
ll = Node('ll')
lr = Node('lr')
rl = Node('rl')
l = Node('l',ll,lr)
r = Node('r',rl)
root = Node('root', l, r)

print(lr.lock())     # expected True
print(ll.lock())     # expected True
print(rl.lock())     # expected True
print(l.lock())      # expected False
print(l.unlock())    # expected False
print(ll.unlock())   # expected True
print(lr.unlock())   # expected True
print(l.lock())      # expected True
print(root.lock())   # expected False
print(root.unlock()) # expected False
print(rl.unlock())   # expected True
print(l.unlock())    # expected True
print(root.lock())   # expected True
print(ll.lock())     # expected False
print(ll.unlock())   # expected False
