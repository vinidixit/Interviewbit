# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 20:48:59 2018

@author: I309535
"""

def rearrange_array(A):
    n = len(A)
    for i in range(n):
        if A[i] < 0 or (A[i]==0 and A[A[i]]<0):## ** IMP: handling 0
            # already visited
            continue
        
        j,temp = A[i],A[i]
        A[i] = -1*A[j]
        print i, A[i]
        while A[j] != i and A[j]>=0:
            k = A[j]
            A[j] = -1*A[k]
            print j,k
            j = k
        A[j] = -1*temp ## IMP: for visit condition
        print 'end:',j,A[j]
        print A,'\n'
    
    for i in range(n):
        if A[i] < 0:
            A[i] = -1*A[i]
          
    return A

A = [1, 2, 7, 0, 9, 3, 6, 8, 5, 4]#[2,0,1,4,3]
print rearrange_array(A)