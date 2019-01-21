'''Implement division of two positive integers without using the
division, multiplication, or modulus operators. Return the quotient as
an integer, ignoring the remainder.
'''

def div(n,m): # divide n by m
    assert m != 0, 'Zero division'
    r = 0
    while n >= m:
        n -= m
        r += 1
    return r

print(div(4,2))
print(div(3,2))
print(div(1,3))
print(div(5,0))
