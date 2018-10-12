# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 09:23:42 2018

@author: I309535
"""
import string
digits = range(1,27)
digits = [str(dig) for dig in digits]
letters = list(string.ascii_uppercase[:27])
dig_letter_map = dict(zip(digits,letters))

### NO out is required
## TC :                1
def ways_to_decode(digits):
    result = [0]    
    find_combinations(digits,0,[],result, len(digits))
    print result
    return result[0]

def find_combinations(digits,ind,out,result,n):
    if ind == n:
        result[0]+=1
        return
    
    size = 1
    while ind+size<=n:
        print ind,size,n
        cur_num = digits[ind:ind+size]
        if cur_num not in dig_letter_map:
            break
        find_combinations(digits,ind+size,out,result,n)
        size += 1

print ways_to_decode('1234')      
            