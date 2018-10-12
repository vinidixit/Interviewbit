# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 21:10:58 2018

@author: I309535
"""

class Solution:
    
    def isPalindrome(self, string):
        i,j = 0,len(string)-1
        while i<j:
            if string[i]!=string[j]:
                return False
            i,j = i+1,j-1
        
        return True
        
    def palPartition(self, A, l, r, partitions, result):
        if l==len(A):
            result.append(list(partitions))
            return
        if r > len(A):
            return
        
        part = A[l:r]
        if self.isPalindrome(part):
            #partitions.append(part) ********* IMP***********
            self.palPartition(A, r, r+1, partitions+[part], result)
            #partitions.remove(part)
        
        self.palPartition(A, l, r+1, partitions, result)
        
        
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        if not A:
            return []
            
        result = []
        self.palPartition(A, 0, 1, [], result)
        return result
        