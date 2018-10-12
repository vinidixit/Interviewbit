# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 15:49:45 2018

@author: I309535
"""

# @param A : list of integers
# @return A after the sort
def sortColors(A):
    counts = [0]*3
    for num in A:
        counts[num]+=1
    ptr = 0
    for i in range(3):
        for j in range(counts[i]):
            A[ptr] = i
            ptr += 1
            
    return A