# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 18:41:09 2018

@author: I309535
"""

class Solution:
    def condition(self,strings, ptrs):
        ch = strings[0][ptrs[0]]
        for i in range(1,len(strings)):
            if ptrs[i]==len(strings[i]) or strings[i][ptrs[i]] != ch:
                return False
        return True
    
    def inc(self, ptrs):
        for i in range(len(ptrs)):
            ptrs[i] += 1
            
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        if not A:
            return ''
            
        ptrs = [0]*len(A)
        while ptrs[0]< len(A[0]) and self.condition(A,ptrs):
            self.inc(ptrs)
        
        return A[0][:ptrs[0]]
        
        