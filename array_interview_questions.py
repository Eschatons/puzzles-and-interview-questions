# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 16:52:11 2016

@author: efron
"""

"""
string interview questions: arrays

"""

"""
find second_highest-number in an integer_array
"""
def max_2(A):
    if len(A) < 2:
        return False
    
    max_1 = max(A[0], A[1])
    max_2 = min(A[0],  A[1])
    
    for a in A:
        if a > max_1:
            max_2 = max_1
            max_1 = a
        elif a > max_2:
            max_2 = a
    return max_2
#print(max_2([1, 8, 13, 1231230, 9123]))       

'''find all pairs of integers in array whose sum is equal to n'''
# assumes we don't want duplicates:
# if we have [2, 2, 3, 3, 5, 0, 5, 6] and we want to sum to 5
# we want only {(0, 5), and (2, 3)}

# O(n), I think.
def array_pairs_that_sum_to(A, n):
    key = set()
    inverse = {}    # dictionary
    pair = set()
    
    for a in A:
        inverse[a] = n-a
        key = key | {a}
    for b in key:
        if inverse[b] in key:
            if inverse[b] < b:
                pair = pair | {(inverse[b], b)}
            else:
                pair = pair | {(b, inverse[b])}
    return sorted(pair)
    

pair = array_pairs_that_sum_to(range(20), 15)
for element in pair:
    print(element, '=', '15')
       