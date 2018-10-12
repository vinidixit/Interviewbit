# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 21:25:34 2018

@author: I309535
"""

class Solution:
    def genUniquePermutations(self, A, curInd, result):
        if curInd == len(A):
            result.append(list(A))
            return
        
        for i in range(curInd,len(A)):
            if i!=curInd and (A[i]==A[curInd] or A[i]==A[i-1]):
                continue
            A[i],A[curInd] = A[curInd],A[i]
            self.genUniquePermutations(A, curInd+1, result)
            A[i],A[curInd] = A[curInd],A[i]
        
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        result = []
        A.sort()
        self.genUniquePermutations(A, 0, result)
        return result