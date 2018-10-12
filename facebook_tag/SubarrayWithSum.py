# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 12:09:23 2018

@author: I309535
"""

#code
def subarrayWithSum(A, target):
    n = len(A)
    if n ==0:
        return -1,-1
        
    i = 0
    cur_sum = A[0]
    j = i+1
    while j < n:
        cur_sum += A[j]
        if cur_sum == target:
            return i+1,j+1
        elif cur_sum>target:
            cur_sum -= A[i]
            i += 1
        j+=1
        
    return -1,-1
