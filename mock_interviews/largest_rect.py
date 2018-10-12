# -*- coding: utf-8 -*-
"""
Created on Sun Apr 01 23:34:40 2018

@author: I309535
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        n = len(A)
        stack = list()
        max_area = 0
        for i in range(n):
            # current element is less than top of stack
            if len(stack)!=0 and A[i] < A[stack[-1]]:
                R = stack[-1]
                while len(stack)!=0 and A[i] < A[stack[-1]]:
                    L = stack.pop()
                    h = A[L]
                    if len(stack)==0:
                        ## cur element is minimum from the beginning
                        cur_area = h*(R+1)
                    else:
                        cur_area = h*(R-stack[-1])
                    max_area = max(max_area,cur_area)
                    print R, L, max_area
                    
            stack.append(i)
            
        if len(stack)!=0:
            R = stack[-1]
            while len(stack)!=0:
                L = stack.pop()
                h=A[L]
                if len(stack)==0:
                    ## cur element is minimum from the beginning
                    cur_area = h*(R+1)
                else:
                    cur_area = h*(R-stack[-1])
                max_area = max(max_area,cur_area)
                        
        return max_area
                        
                        
                        
s = Solution()
A = [6, 2, 5, 4, 5, 1, 6]#[90, 58, 69, 70, 82, 100, 13, 57, 47, 18]
print s.largestRectangleArea(A)                        
                        
                        
                        