# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 15:26:09 2018

@author: I309535
"""

def diff_k(A,B):
    i = 0
    j = 1
    while j < len(A):
        if A[j] - A[i] == B and i != j:
            return 1
        if A[j] - A[i] > B:
            i += 1
        else:
            j += 1
    return 0