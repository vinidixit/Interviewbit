# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:13:22 2018

@author: I309535
"""

# @param A : list of integers
# @return an integer
def maxArea(self, A):
    l,r = 0,len(A)-1
    maxArea = 0
    while l < r:
        curArea = min(A[l],A[r])*(r-l)
        maxArea = max(maxArea,curArea)
        if A[l]<A[r]:
            l += 1
        else:
            r -= 1
            
    return maxArea