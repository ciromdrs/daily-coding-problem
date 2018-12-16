'''Implement an LRU (Least Recently Used) cache. It should be able to be
initialized with a cache size n, and contain the following methods:

    set(key, value): sets key to value. If there are already n items in
        the cache and we are adding a new item, then it should also
        remove the least recently used item.
    get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
'''

'''
Solution: Combine a stack, to store the elements in it, and a hash, to
provide instant access to the stack elements.
Everytime an element is accessed, it must be taken to the end of the
stack.
Everytime an element is inserted, if the stack is full, a pop must be
performed.
'''
