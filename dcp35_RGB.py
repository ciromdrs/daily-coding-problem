'''Given an array of strictly the characters 'R', 'G', and 'B',
segregate the values of the array so that all the Rs come first, the Gs
come second, and the Bs come last. You can only swap elements of the
array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it
should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
'''

def swap(A,i,j):
    aux  = A[i]
    A[i] = A[j]
    A[j] = aux

def segregate(A):
    iR = -1
    iB = len(A)
    while iB >= 0 and A[iB-1] == 'B':
        iB -= 1
    i  = 0
    while iR < iB and i < iB:
        if A[i] == 'R':
            iR += 1
            swap(A,iR,i)
        elif A[i] == 'G':
            i  += 1
        elif A[i] == 'B':
            iB -= 1
            swap(A,iB,i)
        if i <= iR:
            i = iR + 1
    return A

array = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print(segregate(array), segregate(array) == ['R', 'R', 'R', 'G', 'G', 'B', 'B'])

