# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:31:35 2016

@author: efron
"""
## code interview questions
"""
#1 write code to check if a string is a palindrom
"""
def is_palindrome(string):
# O(n)

   if string == string[::-1]:
        return True
   
   else:
        return False
#test:        
        #print(is_palindrome('abccba'))
        #print(is_palindrome('not_a_palindrome'))

"""
2 write method which will remove any given character from a string

"""
#string = 'CASH RULES EVERYTHING AROUND ME! CREAM!'
#newstring = string.replace('S', '$')
#print(newstring)

"""
2. print all permutations of string both iteratvely and recursively


"""

## recursive
def permute(string):
    # recursively permute string by taking each character
    # and inserting in each possible place
    if len(string) < 1:
        return [string]
        
    perms = permute(string[1:])
    char = string[0]
    result = []
    
    for substring in perms:
        
        for n in range(len(substring)+1):
            result.append(''.join([substring[:n], char, substring[n:]]))
    # 
    # turn into set to eliminate repeated elements
    return set(result)


#perm = sorted(list(permute('52341c00')))
#for x in range(50):
#    print(perm[x])


''' find out how to do iterative! '''
"""
3. write a function to find longest palindrome in given string
"""
def find_largest_palindrome(string):
#O(n^2). no way to do it faster, right?

    N = len(string)
    palindrome_length = 1;
    palindrome = False

    for n in range(N):
        for m in range(N):
            substr = string[(0+n):(N-m)]

            if is_palindrome(substr):

                if len(substr) > palindrome_length:
                    palindrome = substr
                    palindrome_length = len(substr)

    return palindrome
        
#palindrome = find_largest_palindrome ('padding_asdasdasedaaibohphobia_padasdasdasdasdasdasdasdasdasding');
#print(palindrome)

"""
5.# how to find first non-repeated character of a given string
"""

def first_non_repeated_char(string):
# O(n).
# easy peasy
    for char in string:
        if char != string[0]:
            return char
        
#print(first_non_repeated_char('aac'))

"""
6. how to count occurance of a given character in a string
"""

def count_character_frequency(string):
    key = set()
    frequency = {}
    for char in string:
        key = key | {char} 

    for char in key:
        frequency[char] = 0

    for char in string:
        frequency[char] += 1

    return [key, frequency]
#[key, frequency] = count_character_frequency('chillax, dude')
#for char in key:
#    print(char, ', ', frequency[char])
    
""" 
7. how to check if two strings are anagrams
"""
def check_if_anagram(string1, string2):
    [key1, freq1] = count_character_frequency(string1)
    [key2, freq2] = count_character_frequency(string2)
    
    if freq1 == freq2:
        return True

    else:
        return False
#print(check_if_anagram('aaabbbccc', 'abcabcabc'))

""" 
check parentheses_balance "() {} []"
"""

def check_parentheses_balance(string):
# we need the count of parentheses to be correct AND the order.
# so a stack is the correct tool.
    stack = []
    left = {'{', '[', '('}
    right = {'}', ')', ']'}
    closure = {
                    '{': '}',
                    '(': ')',
                    '[': ']' }
                   
    for char in string:
        if char in left:
            stack.append(closure[char])

        elif (len(stack) > 0) and (char == stack[-1]):
            stack.pop()

        elif char in right:
            # cut off early to save time
            return False
#        print(stack)

    if len(stack) > 0:
        
        return False        

    else:
        return True  
        
#balance1 = check_parentheses_balance('asds( ( (}} )}}{}}}}))')
#balance2 = check_parentheses_balance('asdasd((({{{[[[[]]]]}}})))')
#print(balance1)
#print(balance2)