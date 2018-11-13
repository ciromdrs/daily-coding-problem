'''Given a dictionary of words and a string made up of those words
(no spaces), return the original sentence in a list. If there is more
than one possible reconstruction, return any of them. If there is no
possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and
the string "thequickbrownfox", you should return ['the', 'quick',
'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and
the string "bedbathandbeyond", return either ['bed', 'bath', 'and',
'beyond'] or ['bedbath', 'and', 'beyond'].
'''

def reconstruct(D, string):
    r = []
    aux = ''
    for c in string:
        aux += c
        if aux in D:
            r.append(aux)
            aux = ''
    if aux != '':
        return None
    return r

s = 'thequickbrownfox'
d = set(['quick', 'brown', 'the', 'fox'])
print(reconstruct(d,s))
    
s = 'bedbathandbeyond'
d = set(['bed', 'bath', 'bedbath', 'and', 'beyond'])
print(reconstruct(d,s))

s = 'asdf'
d = set(['foo', 'bar'])
print(reconstruct(d,s))
