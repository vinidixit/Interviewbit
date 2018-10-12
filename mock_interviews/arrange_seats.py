# -*- coding: utf-8 -*-
"""
Created on Sat Apr 07 09:25:54 2018

@author: I309535
"""

class Solution:
    
    #def find_next_vacant_seat(self,unoccupied_pos):
        
        
        
    #.x..x..x.
    # 1,4,7 = median=4
    #..xx..x - 2 steps
    #..xxx.. - 2 steps
    
    # @param A : string
    # @return an integer
    def seats(self, A):
        n = len(A)
        one_pos = []
        zero_pos = []
        
        for i in range(n):
            if A[i]=='x':
                one_pos.append(i)
            else:
                zero_pos.append(i)
                
        mid = one_pos[len(one_pos)/2]
        lm,rm=None,None
        
        left_vacant_pos = zero_pos[zero_pos<mid]
        right_vacant_pos = zero_pos[zero_pos>mid]
        
        left_occupied_pos = one_pos[one_pos<mid]
        right_occupied_pos = one_pos[one_pos>mid]
        
        
        lo = 0#one_pos[0]
        ro = len(left_occupied_pos)-1#one_pos[-1]
        
        lm = #left_vacant_pos[-1]
        rm = #right_vacant_pos[0]
       
        count_steps = 0
        
        while one_pos[ll] < l:
            if A[ll]=='x':
                count_steps += 1
                lm -= 1
                ll+=1
        
        if rm!=None:
            rr = n-1
            while rr > r:
                if A[rr]=='x':
                    count_steps+=1
                    rm+=1
                    rr-=1
                    
        return count_steps            
        
            
            
            
        
        
        
        
        
                
        