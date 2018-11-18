'''Given a singly linked list and an integer k, remove the kth last
element from the list. k is guaranteed to be smaller than the length of
the list.

The list is very long, so making more than one pass is prohibitively
expensive.

Do this in constant space and in one pass.'''

class Node:
    def __init__ (self, value, next=None):
        self.value = value
        self.next  = next
        
    def show(self):
        print('[',self.value,']-',end='')
        if self.next:
            print('>',end='')
            self.next.show()
        else:
            print('-')

def get_kth_last(k,node,parent):
    if node:
        k_, node_, parent_ = get_kth_last(k, node.next, node)
        if k_ == k:
            return (k_, node_,  parent_)
        if k_+1 == k:
            return (k_+1, node,  parent)
        return (k_+1, None, parent)
    else:
        return (0, None,  parent)

def delete(k,list_):
    root = list_
    index, node, parent = get_kth_last(k,list_,None)
    if index == k:
        if parent:
            parent.next = node.next
        else:
            root = node.next
        node.next = None
    else:
        print('invalid k index')
    return root, node

A = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6))))))
A.show()

A, deleted = delete(1,A)
print('deleted',deleted.value)
A.show()

A, deleted = delete(3,A)
print('deleted',deleted.value)
A.show()

A, deleted = delete(4,A)
print('deleted',deleted.value)
A.show()

