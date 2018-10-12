# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 10:47:35 2018

@author: I309535
"""

class GenerateNumbers:
    def get_num(self, out, B, A):
        num = 0
        power = 0
        for i in range(B-1,-1,-1):
            num += A[out[i]]*pow(10,power)
            power += 1
        
        return num
    
    def is_duplicate(self, out,level, num):
        #print 'check duplicate:',out[0:level], ' for :',num
        return num in out[0:level]
        
    def dig_perm(self, out, level, A, B, C, res):
        
        if level==B:
            num = self.get_num(out, B, A)
            if num < C:
                print num
                res.append(num)
            return
        
        n = len(A)
        for i in range(n):
            dig = A[i]
            if level==0 and dig==0 and B > 1:
                continue
            
            #if level > 0 and dig < A[out[level-1]]:
            #    continue
            
            #if self.is_duplicate(out,level,i):
            #    continue
            
            out[level] = i
            self.dig_perm(out, level+1, A, B, C, res)
            
    
    
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        res = []
        out = [0]*B
        
        self.dig_perm(out, 0, A, B, C, res)
        
        
        
        
        