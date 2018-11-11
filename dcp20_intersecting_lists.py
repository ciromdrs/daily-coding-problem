'''
Given two singly linked lists that intersect at some point, find the
intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
return the node with value 8.

In this example, assume nodes with the same value are the exact same
node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists)
and constant space.'''

def intersection(A,B):
    longer  = None
    shorter = None
    if len(A) > len(B):
        longer  = A
        shorter = B
    else:
        longer  = B
        shorter = A

    offset = len(longer)-len(shorter)
    for i in range(len(shorter)):
        if longer[i+offset] == shorter[i]:
            return longer[i]

A = [3, 7, 8, 10]
B = [99, 1, 8, 10]

print(intersection(A,B))
