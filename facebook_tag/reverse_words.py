# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 21:29:17 2018

@author: I309535
"""

def reverseWords(A):
    words = A.split()
    l,r = 0, len(words)-1
    while l < r:
        tmp = words[l]
        words[l] = words[r]
        words[r] = tmp
        l += 1
        r -= 1
    
    return ' '.join(words)
    

string = "fwbpudnbrozzifml osdt ulc jsx kxorifrhubk ouhsuhf sswz qfho dqmy sn myq igjgip iwfcqq"
print reverseWords(string)