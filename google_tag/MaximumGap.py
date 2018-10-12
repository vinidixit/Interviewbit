# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 23:31:54 2018

@author: I309535
"""

"""
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        if n == 0:
            return -1
            
        LMin = [0]*n
        RMax = [0]*n
        LMin[0] = A[0]
        
        for i in range(1,n):
            LMin[i] = min(LMin[i-1],A[i])
        
        RMax[-1] = A[-1]    
        for i in range(n-2,-1,-1):
            RMax[i] = max(RMax[i+1],A[i])
        
        i,j,maxGap = 0,0,-1
        while j < n and i <=j:
            if LMin[i]<=RMax[j]:
                maxGap = max(maxGap,j-i)
                j += 1
            else:
                i += 1
        
        return maxGap        
                
                
                
                
                
        
        