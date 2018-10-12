# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 14:40:45 2018

@author: I309535
"""
def generateSeq(num):
    digits = str(num)
    res = []
    n = len(digits)
    i = 0
    while i < n:
        cur = digits[i]
        j = i+1
        while j < n  and digits[j]==cur:
            j+=1
        
        count = j-i
        res.append(str(count))
        res.append(cur)
        i = j
    
    return ''.join(res)
        
# @param A : integer
# @return a strings
def countAndSay(A):
    n = 1
    seq = '1'
    for i in range(1,A):
        seq = generateSeq(n)
        n = int(seq)
    return seq