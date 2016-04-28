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
    if string == string[::-1]:
        return True
    else:
        return False
#test:        
        #print(is_palindrome('abccba'))
        #print(is_palindrome('not_a_palindrome'))

## 2 write method which will remove any given character from a string

string = 'ASS!'
newstring = string.replace('S', '$')
print(newstring)

"""
2. print all permujtations of string both iteratvely and recursively
FIND THIS OUT
"""

"""
3. write a function to find longest palindrome in given string
"""
def find_largest_palindrome(string):
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
        
palindrome = find_largest_palindrome ('padding_asdasdasedaaibohphobia_padasdasdasdasdasdasdasdasdasding');
print(palindrome)

"""
5.# how to find first non-repeated character of a given string
"""

def first_non_repeated_char(string):
    char = [a for a in string if a != string[0]]
    return char
print(first_non_repeated_char('aac'))

"""
6. how to count occurance of a given character in a string
"""

def count_character_frequency(string):
    key = set()
    frequency = {}
    for char in string:
        key = key | {char} 
    for repeated_element in key:
        frequency[repeated_element] = 0
    for char in string:
        frequency[char] += 1
    return [key, frequency]

[key, frequency] = count_character_frequency('chillax, dude')
for char in key:
    print(char, ', ', frequency[char])
    
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
print(check_if_anagram('aaabbbccc', 'abcabcabc'))
