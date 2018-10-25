'''
Given the root to a binary tree, implement serialize(root), which
serializes the tree into a string, and deserialize(s), which
deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    def rec(node, trace):
        s = ''
        if node != None:
            s = trace + '=' + node.val + '\n'
            s += rec(node.left, trace + 'l')
            s += rec(node.right, trace + 'r')
        return s
    return rec(root,'')
        
    
def deserialize(serialized):
    def add(node, line):
        i = 0
        parent = node
        while i < len(line):
            if line[i] == 'l': # go left
                parent = node
                node = parent.left
            elif line[i] == 'r': # go right
                parent = node
                node = parent.right
            elif line[i] == '=': # add
                node = Node(line[i+1:])
                if line[i-1] == 'l':
                    parent.left = node
                elif line[i-1] == 'r':
                    parent.right = node
                return
            else:
                print('Error at position %s: %s' % (i,line))
                return
            i += 1
            
    tree = None
    if len(serialized)>0:
        if serialized[0] == '=':
            tree = Node(serialized[1:serialized.index('\n')])
            for l in serialized.split('\n')[1:]:
                add(tree, l)
    return tree

node = Node('root',
    Node('left',
        Node('left.left')),
    Node('right'))
    
s1 = serialize(node)
s2 = serialize(deserialize(s1))

print(s1)
print(s2)
print('s1 == s2',s1 == s2)

assert deserialize(serialize(node)).left.left.val == 'left.left'
