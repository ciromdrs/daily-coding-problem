'''The power set of a set is the set of all its subsets. Write a
function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2},
{3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.'''

def prod(A,B):
    C = []
    for a in A:
        for b in B:
            C.append(a+b)
    return C

def power(S,i):
    if i >= len(S):
        return []
    P1 = [[S[i]]]
    P2 = power(S,i+1)
    P1 += P2 + prod(P1,P2)
    return P1

def power_set(S):
    return [[]] + power(S,0)

S = [1,2,3]

print(power_set(S))
