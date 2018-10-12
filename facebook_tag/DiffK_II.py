# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 14:02:43 2018

@author: I309535
"""

# @param A : tuple of integers
# @param B : integer
# @return an integer
def diffPossible(self, A, B):
    dic = dict()
    for num in A:
        if num in dic:
            dic[num]+=1
        else:
            dic[num]=1
    
    for num in A:
        target1 = B+num
        target2 = num-B
        
        if target1 in dic and (target1!=num or dic[num]>1):
            return 1
        
        if target2 in dic and (target2!=num or dic[num]>1):
            return 1
    
    return 0