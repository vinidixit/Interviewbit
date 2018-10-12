# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 09:22:19 2018

@author: I309535
"""

def uniquePermutations(A,cur_ind,result):
    if cur_ind == len(A):
        result.append(list(A))
        return
    print cur_ind, A
    for i in range(cur_ind,len(A)):
        #if i!=cur_ind and (A[i]==A[cur_ind] or A[i]==A[i-1]):
        #    continue
        # swap
        A[cur_ind],A[i] = A[i],A[cur_ind]
        uniquePermutations(A,cur_ind+1,result)
        A[i],A[cur_ind] = A[cur_ind],A[i]
        
        
A =  [ 10, 9, 10, 9, 10 ]
A.sort()
result = []
uniquePermutations(A,0,result)
print result