# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 15:44:42 2018

@author: I309535
"""

# @param A : tuple of integers
# @param B : tuple of integers
# @return a list of integers
def intersect(self, A, B):
    result = []
    i,j,n1,n2 = 0,0,len(A),len(B)
    while i < n1 and j < n2:
        if A[i] == B[j]:
            result.append(A[i])
            i += 1
            j += 1
        elif A[i]>B[j]:
            j += 1
        else:
            i += 1
    return result