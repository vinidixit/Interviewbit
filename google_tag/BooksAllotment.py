# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 13:30:06 2018

@author: I309535
"""
import math
class Solution:
    def allotmentCondition(self, curAllotment,pagesPerStudent,curPages):
        if curAllotment+curPages < pagesPerStudent:
            return True
        
        if curAllotment+curPages-pagesPerStudent < abs(pagesPerStudent-curAllotment):
            return True
        
        return False
        
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        if not A:
            return -1
        
        studentCnt = 1
        pagesPerStudent = math.ceil(1.0*sum(A)/B)
        curAllotment = 0
        maxAllotment = 0
        for i in range(len(A)):
            if self.allotmentCondition(curAllotment,pagesPerStudent,A[i]):
                curAllotment += A[i]
            else:
                studentCnt+=1
                maxAllotment = max(maxAllotment,curAllotment)
                curAllotment = A[i]
        
        maxAllotment = max(maxAllotment,curAllotment)
        print studentCnt, maxAllotment
        return maxAllotment if studentCnt==B else -1
        
        
A = [ 73, 58, 30, 72, 44, 78, 23, 9 ]
B = 5
print Solution().books(A,B)