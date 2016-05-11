# -*- coding: utf-8 -*-
'''
IMPORT AND OTHER STUFF
'''
import random
import math as M


'''
------------------------------------------------------------------------------
'''
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

            
print('int to string: (512) --> ' + int_to_string(512))

"""
check if number is binary (representation in base 10 contains only 1 and 0)
"""

'''
------------------------------------------------------------------------------
'''
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

'''
------------------------------------------------------------------------------
'''
"""
 find primes under an integer  
"""    
# this is between O(n^2) and O(n*log(n)).
# the limit as n >> infinity is  O(n*log(n))
"""
approach 1: function
"""
def primes_under(N):
    if N < 2:                       # no primes under 2
        return []
    primes = [2]                    
    for n in range(2, N):
        COULD_BE_PRIME = True
        
        for p in primes:
            if (n % p) == 0:
                # no need to check farther
                COULD_BE_PRIME = False
                break
            
        if COULD_BE_PRIME:
            primes.append(n)

    return primes
"""
approach 2: generator (aka, lazy evaluation)
"""
def generate_primes_under(N):
    if N < 2:
        yield []
    else:
        primes = [2]
        for n in range(2, N):
            COULD_BE_PRIME = True

            for p in primes:
                if (n % p) == 0:
                    COULD_BE_PRIME = False
                    break
                
            if COULD_BE_PRIME:
                primes.append(n)
                yield n

'''
------------------------------------------------------------------------------
'''
"""
the power of generators:
"""    
# because we use generators // lazy evaluation, we don't actually calculate all
# these primes. only when they're called for.
def this_many_primes(N):
    prime = generate_primes_under(2**32-1)
    subset = []
    for n in range(N):
        subset.append(next(prime))
    return subset

primes = this_many_primes(2000)

''' 
twin_primes: generator
'''
twin_primes = ((x, x+2) for x in primes if x+2 in primes)

'''
-------------------------------------------------------
'''
#for x in range(300):
#    print(next(twin_primes))

""" 
factor integer w/ crude sieve: 
"""

"""
approach one: iterative function
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
        if N <= p:
        # no need to test remaining primes
            break
    if N > 1:   # remaining factor is prime
        factors.append(N)
    return factors


'''
random semiprimes!
'''
def semi_random_semi_prime():
    temp =  random.sample(primes, 2)
    return temp[0]*temp[1]

#semiPrime = semi_random_semi_prime()
#factors = factor(semiPrime)
#print(''.join(['A somewhat random semiprime is:\n', str(semiPrime), ' = ', 
#      str(factors[0]), '*', str(factors[1])]))


# primes = primes_under(250)
#print([p for p in primes])

""" 
approach 2: iterative generator

"""
# recursive factoring:
def generate_factor(N):
    if N < 0:              
        yield -1
        N = N*-1

    if N == 1:              
        yield []
            
    sqrt = int(N**(.5)+1)
    primes = primes_under(sqrt)

    ## try and deflate integer w/out repeating prime list
    for p in primes:
        if N % p == 0:   
            N = N//p
            yield p
        if N > 1:
            yield N
                          

    
    
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

"""
generative function to create all fibbonaci #s
"""
def fibonnaci_generator():
    lastfib = 0
    fib = 1
    yield fib
    while True:     # neat, right?
        fib, lastfib = fib+lastfib, fib
        yield fib

""" cheatyface"""
GOLDEN_RATIO = 1+M.sqrt(5)

def explicit_fib(N):
    fib = round(((1+M.sqrt(5))**N) - (1-M.sqrt(5))**N)/ ((1 << N)*M.sqrt(5)))
    return fib
fibs = fibonnaci_generator()

print(fibbonaci(50))
print(explicit_fib(50))