'''Implement a stack that has the following methods:

    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack.
        If there are no elements in the stack, then it should throw an
        error or return null.
    max(), which returns the maximum value in the stack currently. If
        there are no elements in the stack, then it should throw an
        error or return null.

Each method should run in constant time.'''

class Stack:
    val_stack = []
    max_stack = []
    
    def push(self, val):
        self.val_stack.append(val)
        m = val
        if len(self.max_stack) > 0:
            m = max(val,self.max_stack[-1])
        self.max_stack.append(m)
        
    def pop(self):
        self.val_stack.pop()
        self.max_stack.pop()
        
    def max(self):
        if len(self.max_stack) > 0:
            return self.max_stack[-1]
        return None

s = Stack()
print(s.max())

s.push(2)
print(s.max())

s.push(4)
print(s.max())

s.push(1)
print(s.max())

s.push(3)
print(s.max())

for i in range(4):
    s.pop()
    print(s.max())

