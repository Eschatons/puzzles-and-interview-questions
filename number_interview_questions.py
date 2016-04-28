# -*- coding: utf-8 -*-

"""
Created on Wed Apr 27 17:22:43 2016

@author: efron
"""

''' bitwise operator'''

'''
 sum of digits in a number
 '''
def int_to_string(N):
#O(n)
    n = 0
    string = ''
    while True:                                 # let's get dangerous!
        n = n + 1
        string = string + str(N % (10**n))[0]
        if 10**n > N or n>500:
            return string[::-1]

            
#print(int_to_string(512))

"""
check if number is binary (representation in base 10 contains only 1 and 0)
"""


""" count number of set bits in given integer """

"""
    do this
"""

""" check if power of two """
#O(log2(n)). could probably be done with bitmasking in a fancy way...
def is_power_of_two(n):
    m = 0
    while n>=2**m:

        if n == 2**m:

            return True
        m += 1
    return False


""" find primes under an integer """    
# this is between O(n^2) and O(n*log(n)).
# the limit as n >> infinity is  O(n*log(n))

def primes_under(N):
    if N < 2:                       # no primes under 2
        return []
    primes = [2]                    
    for n in range(2, N):
        COULD_BE_PRIME = True
        
        for p in primes:
            if (n % p) == 0:
                COULD_BE_PRIME = False
                break
            
        if COULD_BE_PRIME:
            primes.append(n)

    return primes

"""
factor integer w/ crude sieve

"""

# returns non-one prime factors of an integer
# if integer is negative, first factor is "-1"
def factor(N):
    if not isinstance(N, int):
        print('Warning! Input to factor() is a non-integer')
        return []

        
# factoring is hard! between O(n^3) and O(n*log(n)^2)
# if you must do this, do it in a functional language66
    factors = []
    if N < 0:               # negative numbers
        factors.append(-1)
        N = N*-1

    if N == 1:              
        return factors

    sqrt = int(N**(.5)+1)
    primes = primes_under(sqrt)

    ## try and deflate integer w/out repeating prime list
    for p in primes:
        while N % p == 0:   
            factors.append(p)
            N = N//p
    if N > 1:   # remaining factor is prime
        factors.append(N)
    return factors

factors = factor(1.)
print(factors)
# primes = primes_under(250)

#print([p for p in primes])

""" 
nth fibbonaci number
 """
# O(n)
def fibbonaci(N):
    if N < 0:
        print('no negative fibbonaci number')
        raise
    fib = 1
    last_fib = 0
    for n in range(N):
        temp = fib
        fib += last_fib
        last_fib = temp
    return fib

#fib = [fibbonaci(a) for a in range(15)]
#print(fib)