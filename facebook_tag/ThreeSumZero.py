# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:10:54 2018

@author: I309535
"""


def twoSum(A,l,r,target):
    result = []
    last_l = l
    
    while l < r:
        if A[l]+A[r]==target:
            comb = [-target,A[l],A[r]]
            last_l = l
            if len(result)==0 or result[-1]!=comb:
                result.append(comb)
            l += 1
            
        if A[l]+A[r]<target:
            l+=1
        else:
            r -= 1
    return result,last_l
    
# @param A : list of integers
# @return a list of list of integers
def threeSum(A):
    n = len(A)
    result = []
    A.sort()
    i = 0
    
    while i < n-2:
        print i
        comb,last_l = twoSum(A,i+1,n-1,-A[i])
        if len(comb)>0:
            #print comb
            result += comb
        if i+1<n and A[i+1]==A[i]:
            i+=1
            while i < n and A[i]==A[i-1]:
                i+=1
        else:
            i+=1
    return result
        
A = [ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]
print threeSum(A)     
        
        
        
        
        
