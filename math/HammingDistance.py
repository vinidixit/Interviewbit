# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 10:00:43 2018

@author: I309535
"""

class HammingDistance:
    def get_bit_val(self,num,bit_pos):
        mask = 1<<bit_pos
        return 1 if num&mask>0 else 0
        
    
    def hammingDistance_old(self, A):
        n = len(A)
        hamming_distance = 0
        
        for bit_pos in range(32):
            ## bit values in each number for a bit position
            xy=[0,0]
            for i in range(n):
                num = A[i]
                bit_val = self.get_bit_val(num,bit_pos) 
                xy[bit_val]+=1
                
            hamming_distance += 2*xy[0]*xy[1]
        
        return hamming_distance