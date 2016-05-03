# -*- coding: utf-8 -*-
import copy
"""
Created on Tue May  3 13:56:35 2016

@author: Efron
"""
""" 
explain the output of the following code
"""
A0 = dict(sorted(zip(('a','b','c','d','e'),(1,2,3,4,5))))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print("A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))\n", A0)
print('A0 is a dictionary with keys "a", "b", ... "e" corresponding to "1", "2", .. "5"')
print('A1\n', A1)
print('this is a sorted list of elmeents i in range(10 if i in A0). this is empty since A0 contains key-value pairs\n' )
print('A2\n', A2)
print('A3\n', A3)
print('A4\n', A4)
print('A5:{i:i*i} for i in A1:\n', A5)
print('this is a dictionary with keys 0...9 and values 0^2, 1^2, ... 9^2\n')

print('A6 = [[i,i*i] for i in A1]\n', A6)
print(''.join(['this is a list of lists with element 0 in list 0, 1, 2 ... 9\n',
              'element 1 in each list 0^2, 1^2, ... 9^2']))
              
"""
explain the output of the following function
"""

def f(x, l=[]):
    for n in range(x):
        l.append(n*n)
        print(l)
    return l

fa = copy.copy(f(2))    # dereference l from list
fb = f(2)
print("fa = fb, right?", fa == fb)  

"""
 function that produces the expected behavior
"""
def g(x, l = []):
    output = copy.copy(l)   # de-reference
    for n in range(x):
        output.append(n*n)
        print(output)
    return output

print('this function adds 0^2, 1^2, ... x^2 to THE LIST DEFINED when l is called in order, then prints after adding each element')

ga = copy.copy(g(2))
gb = g(2)
print("ga == gb, right?", ga == gb)
