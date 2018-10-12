# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 21:16:50 2018

@author: I309535
"""

class Solution:
    def genPermutations(self, A, curInd, result):
        if curInd == len(A):
            result.append(list(A))
            return
        
        for i in range(curInd,len(A)):
            A[i],A[curInd] = A[curInd],A[i]
            self.genPermutations(A, curInd+1, result)
            A[i],A[curInd] = A[curInd],A[i]
        
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        result = []
        self.genPermutations(A, 0, result)
        return result