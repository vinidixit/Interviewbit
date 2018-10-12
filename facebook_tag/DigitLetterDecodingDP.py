# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 18:17:28 2018

@author: I309535
"""

import string
 
def find_combinations(digits,ind,result,n,dig_letter_map,count):
    count[0]+=1
    if ind == n:
        result[0]+=1
        return 1   
    
    
    comb_count = 0
    for i in range(1,3):
        cur_num = digits[ind:ind+i]    
        if cur_num in dig_letter_map:
            comb_count+=find_combinations(digits,ind+i,result,n,dig_letter_map,count)
    return comb_count
#def find_combinations_iterative(digits,n,dig_letter_map):
    #for i in range(n):
        
def findDigLetterMapCountsDP(digits):
    counts = [0]*len(digits)
    counts[0] = 1 # first digit can make one letter
    for i in range(1,len(digits)):
        num = int(digits[i-1:i+1])
        if num>= 1 and num<=26:
            print num
            counts[i] = counts[i-1]+1
        else:
            counts[i] = counts[i-1]
    print counts
    return counts[-1]
    
    
# @param A : string
# @return an integer
def numDecodings(A):
    count = [0]
    
    digits = range(1,27)
    digits = [str(dig) for dig in digits]
    letters = list(string.ascii_uppercase[:27])
    dig_letter_map = dict(zip(digits,letters))
    #result = [0]
    #print find_combinations(A,0,result,len(A),dig_letter_map,count)
    return findDigLetterMapCountsDP(A)
    #print count[0]
    #return result[0]
    
    
print numDecodings('875361268549483279131')

        
        
        
