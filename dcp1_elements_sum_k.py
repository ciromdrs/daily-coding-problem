'''
Given a list of numbers and a number k, return whether any two numbers
from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since
10 + 7 is 17.

Bonus: Can you do this in one pass?'''

def check(numbers,k):
    wanted = set()
    for n in numbers:
        if n in wanted or k-n in wanted:
            return True
        wanted.add(k-n)
    return False
    
numbers = [10, 15, 3, 7]
k = 17
print(check(numbers,k))
