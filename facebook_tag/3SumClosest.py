# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 09:49:21 2018

@author: I309535
"""
def twoSumClosest(A,target,l,r):
    #l,r = 0,len(A)-1
    best_l,best_r,sum_diff = None,None,None
    
    while l < r:
        if A[l]+A[r]==target:
            return l,r
        cur_sum = A[l]+A[r]
        if sum_diff==None or abs(target-cur_sum)<sum_diff:
            sum_diff = abs(target-cur_sum)
            best_l,best_r = l,r
            
        if A[l]+A[r]<target:
            l += 1
        else:
            r -= 1
            
    return best_l,best_r

    
def threeSumClosest(A,target):
    closest_sum = None
    A.sort()
    sum_diff = None
    r = len(A)-1
    
    for i in range(len(A)-2):
        cur_sum = A[i]
        j,k = twoSumClosest(A,target-cur_sum,i+1,r)
    
        cur_sum += A[j]+A[k]
        if sum_diff == None or abs(target-cur_sum)<sum_diff:
            sum_diff = abs(target-cur_sum)
            closest_sum = cur_sum
            print 'Better:',(i,j,k),(A[i],A[j],A[k]),abs(target-cur_sum)
        else:
            print (i,j,k),(A[i],A[j],A[k]),abs(target-cur_sum)
            
    return closest_sum


A = [ -5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3 ]
A.sort()
print threeSumClosest(A,-1)