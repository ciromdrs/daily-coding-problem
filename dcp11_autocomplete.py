'''Implement an autocomplete system. That is, given a query string s and
a set of all possible query strings, return all strings in the set that
have s as a prefix.

For example, given the query string de and the set of strings [dog,
deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data
structure to speed up queries.
'''

def prefix(s1,s2):
    i = 0
    while i<len(s1) and i<len(s2):
        if s1[i] == s2[i]:
            i += 1
        else:
            break
    return i

class Node:
    def __init__(self, data, complete, children={}):
        self.data = data
        self.complete = complete
        self.children = children
        
    def add(self, new, i):
        add1 = self.data[i:]
        add2 = new[i:]
        self.data = self.data[:i]
        nadd1 = Node(add1,self.complete)
        self.complete = False
        nadd1.children = self.children
        self.children = {add1:nadd1}
        
        for c in self.children:
            j = prefix(add2,c)
            if j > 0:
                self.children[c].add(add2,j)
                break
        else:
            self.children[add2] = Node(add2,True)

    def show(self, level=0):
        print(level*' '+self.data)
        for c in self.children:
            self.children[c].show(level+1)

    
def preprocess(queries):
    roots = []
    for q in queries:
        for r in roots:
            i = prefix(r.data,q)
            if i > 0:
                r.add(q,i)
                break
        else:
            roots.append(Node(q,True))
    return roots


def autocomplete(node,s):
    empty  = s == ''
    stwith = s.startswith(node.data)
    pre = prefix(s,node.data)
    
    if not empty and pre <= 0:
        return []
    
    if empty or pre > 0 :
        res = []
        if len(node.children) > 0:
            for c in node.children:
                new_s = '' if empty else s[pre:]
                for suffix in autocomplete(node.children[c],new_s):
                    res += [node.data + suffix]
        else:
            res = [node.data]
        return res
    return res


s = 'de'
queries = ['dog','deer','deal','monkey','spider','monster']
queries.sort()

tree = preprocess(queries)
    
for r in tree:
    r.show()

for r in tree:
    print(autocomplete(r,s))
