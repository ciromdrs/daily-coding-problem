'''Implement a job scheduler which takes in a function f and an integer
n, and calls f after n milliseconds.
'''
import time
def func1():
    print("func1")
def func2():
    print("func2")

def schedule(func, n):
    time.sleep(n/1000)
    func()

schedule(func1,100)
schedule(func2,3000)
