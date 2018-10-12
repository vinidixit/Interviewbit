# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:19:31 2018

@author: I309535
"""

def permutation(A,out,level,n,result):
    if level == n:
        res = [A[i] for i in out]
        result[str(res)] = res
        return
    
    for i in range(n):
        if exists(out,level,i) :
            continue
        out[level] = i
        permutation(A,out,level+1,n,result)
            
def exists(out,level,i):
    return i in out[:level]
    
# @param A : list of integers
# @return a list of list of integers
def permute(A):
    result = dict()
    n = len(A)
    out = [None]*n
    permutation(A,out,0,n,result)
    return result.values()

print permute([1,1,3])