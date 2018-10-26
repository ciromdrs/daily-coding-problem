'''
Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would
be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected
output would be [2, 3, 6].

Follow-up: what if you can't use division? can you do this in O(n)?
'''

def prod_exc(numbers):
    new = [1]*len(numbers) # [1,1,...,1]
    v = 1
    for i in range(1,len(numbers)):
        v = v*numbers[i-1]
        new[i] = v
    v = 1
    for i in range(len(numbers)-2,-1,-1):
        v = v*numbers[i+1]
        new[i] = new[i]*v
    return new

numbers  = [3, 2, 1]
expected = [2, 3, 6]
print(numbers,'-->',prod_exc(numbers))
assert prod_exc(numbers) == expected

numbers  = [1, 2, 3, 4, 5]
expected = [120, 60, 40, 30, 24]
print(numbers,'-->',prod_exc(numbers))
assert prod_exc(numbers) == expected
