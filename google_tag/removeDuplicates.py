# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 23:15:09 2018

@author: I309535
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
            
        park,prev = None,A[0]
        for i in range(1,len(A)):
            if prev == A[i]:
                if park==None:
                    park = i
            else:
                prev = A[i]
                if park!=None:
                    A[park] = A[i]
                    park+=1    
            
        return len(A) if park==None else park